# Play-Annotation-Generator Annotation Review — Draw_24

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_24`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Slide`
- **Result Frame:** 269
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 122
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `4` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 10 | START | 10 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 10 | START | 10 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 10 | START | 10 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 10 | START | 10 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 10 | START | 10 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 10 | START | 10 | 51 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `4` | 49 | START | 49 | 64 |
| ✅ EXACT | `Action_PassBlock` | RG | `12` | `11` | 52 | START | 52 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `4` | `3` | 52 | START | 52 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `5` | `4` | 52 | START | 65 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `9` | `8` | 52 | START | 52 | 64 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 64 | END | 49 | 64 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `11` | `10` | 69 | START | 69 | 95 |
| ✅ EXACT | `Action_BallCarry` | QB | `11` | `10` | 96 | START | 96 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 131 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 48 | 39 | inferred_complete_timeline |
| `Action_SnapReceive` | 49 | 64 | 16 | inferred_complete_timeline |
| `Action_None` | 65 | 68 | 4 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 69 | 95 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 96 | 269 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 10–43
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 43 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 10–216
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 51 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 79 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 85 | 131 | 47 | inferred_complete_timeline |
| `Action_None` | 132 | 216 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 10–223
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 51 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 64 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 94 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 131 | 22 | inferred_complete_timeline |
| `Action_None` | 132 | 144 | 13 | inferred_complete_timeline |
| `Action_None` | 148 | 223 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 48 | 39 | inferred_complete_timeline |
| `Action_BallSnap` | 49 | 64 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 111 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 113 | 131 | 19 | inferred_complete_timeline |
| `Action_None` | 132 | 269 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 51 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 131 | 80 | inferred_complete_timeline |
| `Action_None` | 132 | 134 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 269 | 129 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 10–237
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 48 | 39 | inferred_complete_timeline |
| `Action_None` | 49 | 128 | 80 | inferred_complete_timeline |
| `Action_None` | 140 | 237 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 10–101
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 48 | 39 | inferred_complete_timeline |
| `Action_None` | 49 | 101 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 48 | 39 | inferred_complete_timeline |
| `Action_None` | 49 | 107 | 59 | inferred_complete_timeline |
| `Action_None` | 109 | 112 | 4 | inferred_complete_timeline |
| `Action_None` | 117 | 269 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 48 | 39 | inferred_complete_timeline |
| `Action_None` | 49 | 178 | 130 | inferred_complete_timeline |
| `Action_None` | 223 | 250 | 28 | inferred_complete_timeline |
| `Action_None` | 254 | 266 | 13 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 10–110
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 48 | 39 | inferred_complete_timeline |
| `Action_None` | 49 | 84 | 36 | inferred_complete_timeline |
| `Action_None` | 87 | 110 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 10–68
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 48 | 39 | inferred_complete_timeline |
| `Action_None` | 49 | 68 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 10–223 | 214 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 46–112 | 67 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 64–109 | 46 | 1 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 89–215 | 98 | 3 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 94–104 | 11 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 97–108 | 12 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 103–139 | 37 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 122–235 | 111 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 138–269 | 132 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 140–239 | 100 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 154–223 | 59 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 210–269 | 60 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 215–241 | 27 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 217–269 | 50 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 220–223 | 4 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 224–269 | 46 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 224–269 | 44 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 224–225 | 2 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 224–269 | 46 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 230–235 | 6 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 232–269 | 36 | 2 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 234–268 | 29 | 2 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 234–239 | 5 | 2 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 234–235 | 2 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 235–269 | 35 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 237–269 | 33 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 238–269 | 32 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 242–269 | 28 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 248–269 | 22 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 251–269 | 18 | 2 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 257–269 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 48: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [49–64], lower_priority='Action_PassBlock' annotated_start=52, effective_Action_PassBlock_start=65.
- ⚠️ Action 'Action_None' range [49-68] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-84] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-223] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [52-79] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-216] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-111] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-128] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-237] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-101] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-107] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [52-64] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-94] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-131] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-144] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-223] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-43] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [96-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [52-131] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-269] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-178] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-250] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-266] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-109] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-178] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-108] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-139] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-190] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-235] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-239] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-192] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-223] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-241] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-255] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-247] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-235] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-241] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-269] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-255] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-268] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-269] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-269] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-269] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.

</details>