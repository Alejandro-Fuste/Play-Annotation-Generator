# Play-Annotation-Generator Annotation Review — Counter_231

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_231`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `16` | `15` |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | offense | `5` | `4` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 55 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 56 | START | 56 | 72 |
| ✅ EXACT | `Action_DownBlock` | RT | `11` | `10` | 57 | START | 57 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `21` | `20` | 57 | START | 73 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `22` | `21` | 57 | START | 57 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `16` | `15` | 57 | START | 57 | 120 |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | `5` | `4` | 57 | START | 57 | 143 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `14` | `13` | 60 | START | 60 | 94 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 72 | END | 56 | 72 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `14` | 86 | START | 86 | 105 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `14` | `13` | 106 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 143 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_SnapReceive` | 56 | 72 | 17 | inferred_complete_timeline |
| `Action_None` | 73 | 85 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 86 | 105 | 20 | inferred_complete_timeline |
| `Action_None` | 106 | 210 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 60 | 94 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 210 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 166 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 57 | 143 | 87 | inferred_complete_timeline |
| `Action_None` | 144 | 169 | 26 | inferred_complete_timeline |
| `Action_None` | 180 | 210 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 210 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 73 | 18 | inferred_complete_timeline |
| `Action_None` | 82 | 127 | 46 | inferred_complete_timeline |
| `Action_None` | 141 | 146 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PullBlock` | 57 | 120 | 64 | inferred_complete_timeline |
| `Action_PullBlock` | 122 | 143 | 22 | inferred_complete_timeline |
| `Action_None` | 144 | 187 | 44 | inferred_complete_timeline |
| `Action_None` | 190 | 210 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_BallSnap` | 56 | 72 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 73 | 89 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 104 | 125 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 134 | 136 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 210 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_DownBlock` | 57 | 76 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 84 | 85 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_DownBlock` | 57 | 98 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 82 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 125 | 70 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 210 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 114 | 59 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 154 | 99 | inferred_complete_timeline |
| `Action_None` | 165 | 177 | 13 | inferred_complete_timeline |
| `Action_None` | 181 | 210 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 210 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 210 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 210 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 210 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 210 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 143 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 3–46 | 9 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 80–210 | 116 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 102–210 | 109 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 142–210 | 69 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 142–210 | 64 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 145–210 | 54 | 4 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 156–210 | 55 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 162–210 | 40 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 178–193 | 6 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 182–210 | 29 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 193–210 | 18 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `16` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `14` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '13' has invalid range: start=106, end=94. Clamping end to start.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [56–72], lower_priority='Action_DownBlock' annotated_start=57, effective_Action_DownBlock_start=73.
- ⚠️ Action 'Action_None' range [56-166] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-169] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-154] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-177] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-125] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-73] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-127] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-146] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [57-98] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [60-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [57-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-187] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-114] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [73-89] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [104-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [134-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [139-140] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [57-76] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [84-85] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-4] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-46] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-125] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-171] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '34' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>