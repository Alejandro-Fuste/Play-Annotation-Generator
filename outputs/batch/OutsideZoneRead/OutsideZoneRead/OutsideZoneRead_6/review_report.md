# Play-Annotation-Generator Annotation Review — OutsideZoneRead_6

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_6`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `8` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 52 |
| ✅ EXACT | `Action_PressEdge` | RB | `6` | `6` | 53 | START | 53 | 88 |
| ✅ EXACT | `Action_ZoneBlock` | C | `13` | `13` | 53 | START | 53 | 115 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `4` | 53 | START | 53 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `7` | 53 | START | 53 | 65 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `8` | 53 | START | 53 | 115 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `5` | `5` | 63 | START | 63 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `5` | `5` | 76 | START | 76 | 79 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 63 | 75 | 13 | inferred_complete_timeline |
| `Action_Keep` | 76 | 79 | 4 | inferred_complete_timeline |
| `Action_Keep` | 82 | 123 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PressEdge` | 53 | 88 | 36 | inferred_complete_timeline |
| `Action_None` | 89 | 113 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 127 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 115 | 63 | inferred_complete_timeline |
| `Action_None` | 116 | 122 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 115 | 63 | inferred_complete_timeline |
| `Action_None` | 116 | 121 | 6 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 115 | 63 | inferred_complete_timeline |
| `Action_None` | 116 | 120 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 65 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 115 | 44 | inferred_complete_timeline |
| `Action_None` | 116 | 120 | 5 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 136 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 123 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 129 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 124 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 130 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 116 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 120 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 232 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 238 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 244 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 253 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 299 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 124 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–129 | 126 | 2 | Undefined position; Undefined team |
| `16` | `31` | Position_Unknown | Team_Unknown | 124–129 | 6 | 1 | Undefined position; Undefined team |
| `17` | `38` | Position_Unknown | Team_Unknown | 126–129 | 4 | 1 | Undefined position; Undefined team |
| `18` | `41` | Position_Unknown | Team_Unknown | 128–129 | 2 | 1 | Undefined position; Undefined team |
| `19` | `46` | Position_Unknown | Team_Unknown | 131–299 | 148 | 5 | Undefined position; Undefined team |
| `20` | `47` | Position_Unknown | Team_Unknown | 131–136 | 6 | 1 | Undefined position; Undefined team |
| `21` | `48` | Position_Unknown | Team_Unknown | 131–139 | 9 | 1 | Undefined position; Undefined team |
| `22` | `50` | Position_Unknown | Team_Unknown | 131–132 | 2 | 1 | Undefined position; Undefined team |
| `23` | `51` | Position_Unknown | Team_Unknown | 133–134 | 2 | 1 | Undefined position; Undefined team |
| `24` | `55` | Position_Unknown | Team_Unknown | 170–223 | 44 | 2 | Undefined position; Undefined team |
| `25` | `58` | Position_Unknown | Team_Unknown | 198–299 | 100 | 3 | Undefined position; Undefined team |
| `26` | `60` | Position_Unknown | Team_Unknown | 217–294 | 76 | 2 | Undefined position; Undefined team |
| `27` | `62` | Position_Unknown | Team_Unknown | 228–299 | 70 | 2 | Undefined position; Undefined team |
| `28` | `63` | Position_Unknown | Team_Unknown | 231–244 | 14 | 1 | Undefined position; Undefined team |
| `29` | `65` | Position_Unknown | Team_Unknown | 237–299 | 62 | 2 | Undefined position; Undefined team |
| `30` | `67` | Position_Unknown | Team_Unknown | 238–299 | 62 | 1 | Undefined position; Undefined team |
| `31` | `71` | Position_Unknown | Team_Unknown | 252–299 | 47 | 2 | Undefined position; Undefined team |
| `32` | `75` | Position_Unknown | Team_Unknown | 254–299 | 46 | 1 | Undefined position; Undefined team |
| `33` | `76` | Position_Unknown | Team_Unknown | 255–275 | 21 | 1 | Undefined position; Undefined team |
| `34` | `78` | Position_Unknown | Team_Unknown | 266–299 | 34 | 1 | Undefined position; Undefined team |
| `35` | `80` | Position_Unknown | Team_Unknown | 277–299 | 21 | 2 | Undefined position; Undefined team |
| `36` | `81` | Position_Unknown | Team_Unknown | 280–299 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-104] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-116] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-120] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-232] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-238] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-244] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-253] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-299] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-124] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-122] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [76-79] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [82-123] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-113] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-65] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-136] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-124] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-127] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-121] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-114] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-123] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-129] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-243] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-254] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-266] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-290] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-139] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-189] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-223] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-255] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-249] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-294] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-286] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-244] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-259] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-287] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-275] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-299] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-284] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>