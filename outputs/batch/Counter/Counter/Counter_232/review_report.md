# Play-Annotation-Generator Annotation Review — Counter_232

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_232`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `10` | `9` |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | offense | `16` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `16` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `17` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 57 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 58 | START | 58 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `13` | `12` | 60 | START | 60 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `15` | `14` | 60 | START | 74 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `4` | `3` | 60 | START | 60 | 75 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `12` | `11` | 60 | START | 60 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `10` | `9` | 60 | START | 60 | 97 |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | `16` | `15` | 60 | START | 60 | 127 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 73 | END | 58 | 73 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `4` | 88 | START | 88 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `12` | `11` | 112 | START | 112 | 168 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 143 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_SnapReceive` | 58 | 73 | 16 | inferred_complete_timeline |
| `Action_None` | 74 | 87 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 88 | 111 | 24 | inferred_complete_timeline |
| `Action_None` | 112 | 127 | 16 | inferred_complete_timeline |
| `Action_None` | 154 | 195 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 60 | 111 | 52 | inferred_complete_timeline |
| `Action_BallCarry` | 112 | 168 | 57 | inferred_complete_timeline |
| `Action_BallCarry` | 170 | 174 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 122 | 65 | inferred_complete_timeline |
| `Action_None` | 125 | 135 | 11 | inferred_complete_timeline |
| `Action_None` | 138 | 151 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 60 | 127 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 103 | 46 | inferred_complete_timeline |
| `Action_None` | 112 | 121 | 10 | inferred_complete_timeline |
| `Action_None` | 137 | 210 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PullBlock` | 60 | 97 | 38 | inferred_complete_timeline |
| `Action_PullBlock` | 99 | 109 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_BallSnap` | 58 | 73 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 74 | 83 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 86 | 115 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 120 | 129 | 10 | inferred_complete_timeline |
| `Action_None` | 170 | 173 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 75 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 80 | 83 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 112 | 143 | 32 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_None` | 155 | 165 | 11 | inferred_complete_timeline |
| `Action_None` | 168 | 173 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 89 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 91 | 97 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 101 | 143 | 43 | inferred_complete_timeline |
| `Action_None` | 144 | 148 | 5 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 156 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 128 | 71 | inferred_complete_timeline |
| `Action_None` | 133 | 165 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 101 | 44 | inferred_complete_timeline |
| `Action_None` | 107 | 112 | 6 | inferred_complete_timeline |
| `Action_None` | 115 | 127 | 13 | inferred_complete_timeline |
| `Action_None` | 131 | 137 | 7 | inferred_complete_timeline |
| `Action_None` | 139 | 159 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 88 | 31 | inferred_complete_timeline |
| `Action_None` | 113 | 170 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 156 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 174 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 183 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 155 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 41–81 | 31 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 57–80 | 5 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 60–105 | 14 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 73–148 | 76 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 104–118 | 15 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 126–163 | 38 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 141–167 | 27 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 144–161 | 14 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 149–171 | 23 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 164–167 | 4 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 207–210 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [58–73], lower_priority='Action_DownBlock' annotated_start=60, effective_Action_DownBlock_start=74.
- ⚠️ Action 'Action_None' range [58-156] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-174] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-155] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [60-75] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [77-78] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [80-83] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [112-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-165] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-127] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-128] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-165] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-183] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-156] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-88] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-170] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [60-97] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [99-109] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-103] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [60-111] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [112-168] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [170-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [60-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [91-97] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-148] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-137] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [74-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [86-115] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [120-129] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [60-127] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-122] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-135] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-46] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 58, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [58-78] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 58, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [58-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-62] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-105] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-148] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-118] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-163] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-167] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-161] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-171] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.

</details>