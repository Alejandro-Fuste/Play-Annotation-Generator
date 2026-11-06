# Play-Annotation-Generator Annotation Review — OutsideZoneRead_93

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_93`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | Position_Unknown | Team_Unknown | `11` | `11` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 17 | START | 17 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 17 | START | 17 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 17 | START | 17 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 17 | START | 17 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 17 | START | 17 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 17 | START | 17 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 17 | START | 17 | 76 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `0` | `0` | 62 | START | 62 | 115 |
| ✅ EXACT | `Action_ZoneBlock` | C | `10` | `10` | 62 | START | 62 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `3` | 62 | START | 62 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `5` | `5` | 62 | START | 62 | 78 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `8` | 62 | START | 62 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | Position_Unknown | `11` | `11` | 66 | START | 66 | 117 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `9` | `9` | 77 | START | 77 | 83 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 84 | START | 84 | 101 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 17–166
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 76 | 60 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 77 | 83 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 84 | 101 | 18 | inferred_complete_timeline |
| `Action_None` | 102 | 166 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 17–213
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 88 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 97 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 103 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 213 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 17–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 61 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 115 | 54 | inferred_complete_timeline |
| `Action_None` | 116 | 269 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 17–98
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 61 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 89 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 98 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 17–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 61 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 115 | 54 | inferred_complete_timeline |
| `Action_None` | 116 | 269 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 17–207
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 61 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 78 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 115 | 35 | inferred_complete_timeline |
| `Action_None` | 116 | 163 | 48 | inferred_complete_timeline |
| `Action_None` | 166 | 207 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 17–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 61 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 115 | 54 | inferred_complete_timeline |
| `Action_None` | 116 | 269 | 154 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 17–242
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 113 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 128 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 149 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 158 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 171 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 180 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 242 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 17–162
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 111 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 156 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 162 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 17–269
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 117 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 127 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 269 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 17–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 269 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 17–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 269 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 17–89
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 89 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 17–269 | 246 | 5 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 111–266 | 156 | 1 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 129–269 | 141 | 1 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 136–207 | 71 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 137–269 | 110 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 143–269 | 127 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 154–200 | 47 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 156–269 | 114 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 164–199 | 14 | 5 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 166–269 | 104 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 171–188 | 12 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 185–186 | 2 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 203–269 | 67 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 213–217 | 5 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 216–269 | 54 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 216–218 | 3 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 233–239 | 7 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 236–269 | 32 | 3 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 238–258 | 16 | 3 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 241–269 | 28 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 256–269 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 188: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [17-88] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-97] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-103] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-108] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-213] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-111] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-156] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-162] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-89] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-98] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-128] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-149] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-158] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-242] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-78] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-163] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-207] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-166] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-115] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [66-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-263] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-89] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-266] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-203] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-207] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-138] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-200] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-166] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-171] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-174] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-190] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-199] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-177] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-188] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-186] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-218] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-239] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-246] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-250] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-240] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-255] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-252] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>