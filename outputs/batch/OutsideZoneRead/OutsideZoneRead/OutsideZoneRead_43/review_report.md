# Play-Annotation-Generator Annotation Review — OutsideZoneRead_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_43`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 449
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 133
- **Validation Warnings:** 187
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 111
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `11` | 85 | START | 85 | 126 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `13` | 85 | START | 85 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 85 | START | 106 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `4` | 85 | START | 85 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `8` | 85 | START | 85 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `9` | `9` | 93 | START | 93 | 110 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `7` | `7` | 97 | START | 97 | 107 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `7` | 113 | START | 113 | 116 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 97 | 107 | 11 | inferred_complete_timeline |
| `Action_None` | 108 | 112 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 113 | 116 | 4 | inferred_complete_timeline |
| `Action_None` | 120 | 122 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PressEdge` | 93 | 110 | 18 | inferred_complete_timeline |
| `Action_PressEdge` | 117 | 144 | 28 | inferred_complete_timeline |
| `Action_None` | 145 | 154 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 85 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 122 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 188 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 210 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 261 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 119 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 160 | 36 | inferred_complete_timeline |
| `Action_None` | 161 | 292 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 102 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 160 | 25 | inferred_complete_timeline |
| `Action_None` | 161 | 173 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 125 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 126 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 134 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 139 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 155 | 71 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |
| `Action_None` | 214 | 222 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–308
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 308 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 197 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 266 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 318 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 165 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 183 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 243 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 82–99 | 18 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 89–91 | 3 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 94–130 | 12 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 99–125 | 9 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 113–125 | 13 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 133–192 | 44 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 138–449 | 296 | 6 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 138–310 | 150 | 5 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 147–156 | 10 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 147–330 | 159 | 5 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 150–162 | 13 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 156–203 | 48 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 180–237 | 58 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 181–449 | 234 | 7 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 201–257 | 44 | 5 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 206–449 | 239 | 5 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 207–449 | 243 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 207–353 | 133 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 208–308 | 88 | 3 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 223–372 | 150 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 243–440 | 165 | 5 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 245–255 | 11 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 254–259 | 6 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 277–339 | 63 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 289–449 | 146 | 8 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 311–449 | 138 | 2 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 374–440 | 67 | 1 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 407–427 | 13 | 2 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 423–449 | 25 | 2 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 429–449 | 21 | 1 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 436–440 | 5 | 1 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 441–449 | 9 | 1 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 443–449 | 6 | 2 | Undefined position; Undefined team |
| `48` | `69` | Position_Unknown | Team_Unknown | 443–444 | 2 | 1 | Undefined position; Undefined team |
| `49` | `70` | Position_Unknown | Team_Unknown | 448–449 | 2 | 1 | Undefined position; Undefined team |
| `50` | `71` | Position_Unknown | Team_Unknown | 448–449 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 114 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-159] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-165] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-183] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-243] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-85] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-214] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-318] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-106] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-197] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-266] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-119] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-292] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-122] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-188] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-261] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-169] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [113-116] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-105] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-173] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [93-110] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-136] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-308] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-126] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [137-139] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-155] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-222] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-99] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-96] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-155] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-192] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-227] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-242] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-252] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-405] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-417] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-176] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-190] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-230] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-246] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-310] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-156] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-152] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-230] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-294] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-330] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-162] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-203] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-237] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-219] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-232] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-329] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-417] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-420] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-216] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-228] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-235] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-257] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-237] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-265] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-353] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-360] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-449] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-271] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-353] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-213] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-228] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-308] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-372] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-261] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-358] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-366] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-397] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-440] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-255] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-259] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-339] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-313] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-330] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-386] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-390] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-426] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-439] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-442] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-368] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-449] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-440] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-414] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-427] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-430] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [429-449] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-440] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-446] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-444] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [448-449] for track '49' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.

</details>