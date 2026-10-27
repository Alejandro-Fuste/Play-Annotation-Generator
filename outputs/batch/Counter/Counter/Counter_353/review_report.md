# Play-Annotation-Generator Annotation Review — Counter_353

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_353`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `17` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `14` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 44 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 45 | START | 45 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `19` | `18` | 48 | START | 48 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `20` | `19` | 48 | START | 48 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `21` | `20` | 48 | START | 58 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `22` | `21` | 48 | START | 48 | 95 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `17` | `16` | 48 | START | 48 | 129 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 57 | END | 45 | 57 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `8` | 62 | START | 62 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `15` | `14` | 86 | START | 86 | 107 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 129 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_SnapReceive` | 45 | 57 | 13 | inferred_complete_timeline |
| `Action_None` | 58 | 61 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 62 | 85 | 24 | inferred_complete_timeline |
| `Action_None` | 86 | 146 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_BallCarry` | 86 | 107 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 124 | 125 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 174 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 161 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 132 | 88 | inferred_complete_timeline |
| `Action_None` | 135 | 138 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 149 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 48 | 129 | 82 | inferred_complete_timeline |
| `Action_None` | 130 | 158 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PullBlock` | 48 | 95 | 48 | inferred_complete_timeline |
| `Action_PullBlock` | 100 | 129 | 30 | inferred_complete_timeline |
| `Action_None` | 130 | 153 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_BallSnap` | 45 | 57 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 58 | 61 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 66 | 78 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 96 | 97 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 48 | 68 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 71 | 107 | 37 | inferred_complete_timeline |
| `Action_DownBlock` | 129 | 129 | 1 | inferred_complete_timeline |
| `Action_None` | 130 | 160 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 48 | 61 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 78 | 107 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 109 | 127 | 19 | inferred_complete_timeline |
| `Action_None` | 134 | 171 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 153 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 109 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 107 | 63 | inferred_complete_timeline |
| `Action_None` | 142 | 155 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 164 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 120 | 76 | inferred_complete_timeline |
| `Action_None` | 127 | 133 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 105 | 61 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_None` | 126 | 150 | 25 | inferred_complete_timeline |
| `Action_None` | 152 | 155 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 180 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 158 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 135 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 175 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 180 | 136 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 123–180 | 58 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 125–180 | 56 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 125–150 | 22 | 4 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 137–153 | 17 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 142–147 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (7 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [45–57], lower_priority='Action_DownBlock' annotated_start=48, effective_Action_DownBlock_start=58.
- ⚠️ Action 'Action_None' range [45-105] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-174] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-161] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-158] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [62-85] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-146] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-135] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-133] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-109] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [86-107] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [124-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [48-129] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-158] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-107] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-155] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [48-61] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [78-107] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [109-127] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-171] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [48-68] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [71-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 130, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [130-160] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [58-61] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [63-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [66-78] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [96-97] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [48-95] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-180] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-153] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-147] for track '26' has 1 frames without a visible bounding box.
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

</details>