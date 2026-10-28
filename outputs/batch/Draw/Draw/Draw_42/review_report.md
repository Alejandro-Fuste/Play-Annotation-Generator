# Play-Annotation-Generator Annotation Review — Draw_42

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_42`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 104
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `13` | `12` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `2` | `1` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `13` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 37 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `8` | 38 | START | 38 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `10` | `9` | 41 | START | 41 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `13` | `12` | 41 | START | 54 | 60 |
| ✅ EXACT | `Action_PassBlock` | RG | `2` | `1` | 41 | START | 41 | 117 |
| ✅ EXACT | `Action_PassBlock` | RT | `7` | `6` | 41 | START | 41 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `9` | `8` | 41 | START | 53 | 69 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 52 | END | 38 | 52 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `5` | `4` | 55 | START | 55 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `5` | `4` | 85 | START | 85 | 128 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 117 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–234
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_SnapReceive` | 38 | 52 | 15 | inferred_complete_timeline |
| `Action_None` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 55 | 84 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 85 | 128 | 44 | inferred_complete_timeline |
| `Action_BallCarry` | 135 | 137 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 143 | 182 | 40 | inferred_complete_timeline |
| `Action_BallCarry` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 212 | 234 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 101 | 61 | inferred_complete_timeline |
| `Action_PassBlock` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 117 | 3 | inferred_complete_timeline |
| `Action_None` | 118 | 239 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 54–127
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PassBlock` | 54 | 60 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 71 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 98 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 109 | 117 | 9 | inferred_complete_timeline |
| `Action_None` | 118 | 118 | 1 | inferred_complete_timeline |
| `Action_None` | 124 | 127 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_BallSnap` | 38 | 52 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 69 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 117 | 47 | inferred_complete_timeline |
| `Action_None` | 118 | 137 | 20 | inferred_complete_timeline |
| `Action_None` | 139 | 170 | 32 | inferred_complete_timeline |
| `Action_None` | 177 | 239 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 117 | 77 | inferred_complete_timeline |
| `Action_None` | 118 | 118 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 117 | 77 | inferred_complete_timeline |
| `Action_None` | 118 | 182 | 65 | inferred_complete_timeline |
| `Action_None` | 184 | 239 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 116 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 147 | 110 | inferred_complete_timeline |
| `Action_None` | 149 | 152 | 4 | inferred_complete_timeline |
| `Action_None` | 159 | 185 | 27 | inferred_complete_timeline |
| `Action_None` | 195 | 202 | 8 | inferred_complete_timeline |
| `Action_None` | 227 | 239 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 239 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 47 | 10 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 94 | 57 | inferred_complete_timeline |
| `Action_None` | 98 | 101 | 4 | inferred_complete_timeline |
| `Action_None` | 113 | 116 | 4 | inferred_complete_timeline |
| `Action_None` | 122 | 239 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 100 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 2–60 | 33 | 5 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 66–239 | 170 | 2 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 86–93 | 8 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 108–109 | 2 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 117–118 | 2 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 138–239 | 102 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 139–239 | 91 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 140–239 | 88 | 7 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 150–174 | 18 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 150–205 | 56 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 167–239 | 58 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 174–239 | 63 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 176–216 | 41 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 180–239 | 60 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 185–239 | 55 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 196–239 | 44 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 200–202 | 3 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 219–221 | 3 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 226–239 | 13 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 230–239 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [38–52], lower_priority='Action_PassBlock' annotated_start=41, effective_Action_PassBlock_start=53.
- ⚠️ Action 'Action_None' range [38-116] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '1' starts at frame 118, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [118-118] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-147] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-185] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-202] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [85-128] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [135-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [143-182] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [209-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [212-234] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-94] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-182] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-100] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-69] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-170] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [104-105] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-47] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-7] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 38, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [38-38] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-60] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-71] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-98] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 118, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [118-118] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-190] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-203] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-175] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-181] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-199] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-224] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-165] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-205] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-193] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-182] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-216] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-234] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.

</details>