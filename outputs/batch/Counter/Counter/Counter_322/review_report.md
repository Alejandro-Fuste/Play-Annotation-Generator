# Play-Annotation-Generator Annotation Review — Counter_322

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_322`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_DownBlock` | TE | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_DownBlock` | DT2 | defense | `7` | `6` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 49 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 47 | START | 47 | 63 |
| ✅ EXACT | `Action_DownBlock` | TE | `11` | `10` | 50 | START | 50 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `14` | `13` | 50 | START | 50 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `15` | `14` | 50 | START | 64 | 73 |
| ✅ EXACT | `Action_DownBlock` | DT2 | `7` | `6` | 50 | START | 50 | 130 |
| ✅ EXACT | `Action_PullBlock` | RG | `9` | `8` | 50 | START | 50 | 130 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `13` | `12` | 50 | START | 50 | 118 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 63 | END | 47 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `4` | `3` | 90 | START | 90 | 233 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 130 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 63 | 17 | inferred_complete_timeline |
| `Action_None` | 64 | 89 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 90 | 233 | 144 | inferred_complete_timeline |
| `Action_BallCarry` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 124 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_DownBlock` | 50 | 130 | 81 | inferred_complete_timeline |
| `Action_None` | 131 | 178 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_DownBlock` | 50 | 73 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 82 | 130 | 49 | inferred_complete_timeline |
| `Action_None` | 131 | 222 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_BallSnap` | 47 | 63 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 64 | 73 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 77 | 98 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 100 | 130 | 31 | inferred_complete_timeline |
| `Action_None` | 131 | 197 | 67 | inferred_complete_timeline |
| `Action_None` | 202 | 239 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PullBlock` | 50 | 130 | 81 | inferred_complete_timeline |
| `Action_None` | 131 | 239 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 50 | 118 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 239 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 61 | 15 | inferred_complete_timeline |
| `Action_None` | 63 | 66 | 4 | inferred_complete_timeline |
| `Action_None` | 69 | 110 | 42 | inferred_complete_timeline |
| `Action_None` | 112 | 119 | 8 | inferred_complete_timeline |
| `Action_None` | 123 | 202 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 56 | 10 | inferred_complete_timeline |
| `Action_None` | 63 | 65 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_DownBlock` | 50 | 130 | 81 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 55 | 9 | inferred_complete_timeline |
| `Action_None` | 59 | 95 | 37 | inferred_complete_timeline |
| `Action_None` | 116 | 119 | 4 | inferred_complete_timeline |
| `Action_None` | 125 | 130 | 6 | inferred_complete_timeline |
| `Action_None` | 134 | 138 | 5 | inferred_complete_timeline |
| `Action_None` | 141 | 239 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 53 | 7 | inferred_complete_timeline |
| `Action_None` | 67 | 239 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 108 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 82 | 36 | inferred_complete_timeline |
| `Action_None` | 87 | 119 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 100 | 54 | inferred_complete_timeline |
| `Action_None` | 108 | 113 | 6 | inferred_complete_timeline |
| `Action_None` | 116 | 239 | 124 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–118 | 119 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 37–83 | 27 | 6 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 87–191 | 34 | 4 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 117–239 | 123 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 118–128 | 5 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 127–239 | 108 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 127–141 | 13 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 128–239 | 111 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 144–186 | 21 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 153–193 | 40 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 198–239 | 41 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 215–216 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 217–219 | 3 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 221–239 | 19 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 222–227 | 6 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 646: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [47–63], lower_priority='Action_DownBlock' annotated_start=50, effective_Action_DownBlock_start=64.
- ⚠️ Action 'Action_None' range [47-118] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-53] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-233] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [237-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-124] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-82] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-119] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [50-130] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-113] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [50-130] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-178] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-55] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-95] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-130] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-138] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [50-118] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [50-73] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [78-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [82-130] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-222] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [64-73] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [77-98] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-197] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-110] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-56] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-41] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-46] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 47, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [47-47] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-83] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-104] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-119] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-225] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-134] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-141] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-160] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-193] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-229] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-239] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.

</details>