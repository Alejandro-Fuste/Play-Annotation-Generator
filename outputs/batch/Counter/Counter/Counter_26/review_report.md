# Play-Annotation-Generator Annotation Review — Counter_26

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_26`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | SAF | defense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF | defense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `12` | `11` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `1` | `0` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 51 |
| ✅ EXACT | `Action_BallSnap` | SAF | `14` | `13` | 47 | START | 47 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF | `14` | `13` | 52 | START | 52 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `12` | `11` | 52 | START | 52 | 64 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `9` | `8` | 52 | START | 52 | 92 |
| ✅ EXACT | `Action_SnapReceive` | QB | `1` | `0` | 64 | END | 47 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `1` | `0` | 76 | START | 76 | 80 |
| ✅ EXACT | `Action_BallCarry` | RB | `3` | `2` | 109 | START | 109 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 124 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 64 | 18 | inferred_complete_timeline |
| `Action_None` | 65 | 75 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 76 | 80 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 88 | 108 | 21 | inferred_complete_timeline |
| `Action_None` | 109 | 210 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_BallCarry` | 109 | 210 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 52 | 92 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 123 | 77 | inferred_complete_timeline |
| `Action_None` | 125 | 154 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PullBlock` | 52 | 64 | 13 | inferred_complete_timeline |
| `Action_PullBlock` | 66 | 88 | 23 | inferred_complete_timeline |
| `Action_PullBlock` | 100 | 124 | 25 | inferred_complete_timeline |
| `Action_None` | 125 | 210 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 142 | 96 | inferred_complete_timeline |
| `Action_None` | 145 | 152 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 62 | 16 | inferred_complete_timeline |
| `Action_None` | 90 | 130 | 41 | inferred_complete_timeline |
| `Action_None` | 136 | 203 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 155 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 90 | 44 | inferred_complete_timeline |
| `Action_None` | 95 | 98 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 150 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 94 | 48 | inferred_complete_timeline |
| `Action_None` | 99 | 210 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 100 | 54 | inferred_complete_timeline |
| `Action_None` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_None` | 113 | 142 | 30 | inferred_complete_timeline |
| `Action_None` | 145 | 210 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 175 | 129 | inferred_complete_timeline |
| `Action_None` | 177 | 179 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_BallSnap` | 47 | 51 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 52 | 72 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 74 | 78 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 89 | 93 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 95 | 104 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 108 | 111 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 124 | 12 | inferred_complete_timeline |
| `Action_None` | 125 | 210 | 86 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–99 | 100 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 8–37 | 30 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 48–49 | 2 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 91–210 | 120 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 117–147 | 31 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 127–162 | 36 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 140–167 | 28 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 141–179 | 19 | 4 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 147–210 | 63 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 148–210 | 63 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 150–210 | 61 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 160–210 | 51 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 161–210 | 50 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 176–177 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 188–198 | 6 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 198–201 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `1` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 54: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_Handoff' range [76-80] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [83-86] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [88-108] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-155] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [109-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-99] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-94] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-90] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-175] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-142] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-152] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [52-92] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-150] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-123] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-154] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [52-64] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [66-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [100-124] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [52-72] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [74-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [89-93] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [95-104] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [108-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-62] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-203] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-37] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-147] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-167] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-145] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-163] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.

</details>