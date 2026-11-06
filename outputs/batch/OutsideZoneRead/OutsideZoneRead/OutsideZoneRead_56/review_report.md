# Play-Annotation-Generator Annotation Review — OutsideZoneRead_56

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_56`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `6` | `6` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `8` | `8` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `0` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 69 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `0` | `0` | 67 | START | 67 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `10` | 67 | START | 67 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `14` | `14` | 67 | START | 67 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `6` | `6` | 67 | START | 67 | 93 |
| ✅ EXACT | `Action_PressEdge` | RB | `8` | `8` | 70 | START | 70 | 127 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `4` | `4` | 81 | START | 81 | 89 |
| ✅ EXACT | `Action_Handoff` | QB | `4` | `4` | 90 | START | 90 | 98 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 81 | 89 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 90 | 98 | 9 | inferred_complete_timeline |
| `Action_None` | 99 | 135 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PressEdge` | 70 | 127 | 58 | inferred_complete_timeline |
| `Action_None` | 128 | 206 | 79 | inferred_complete_timeline |
| `Action_None` | 208 | 269 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 83 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 96 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 112 | 11 | inferred_complete_timeline |
| `Action_None` | 122 | 170 | 49 | inferred_complete_timeline |
| `Action_None` | 176 | 201 | 26 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 93 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 98 | 4 | inferred_complete_timeline |
| `Action_None` | 115 | 129 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 110 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_None` | 114 | 123 | 10 | inferred_complete_timeline |
| `Action_None` | 127 | 133 | 7 | inferred_complete_timeline |
| `Action_None` | 136 | 138 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 113 | 47 | inferred_complete_timeline |
| `Action_None` | 114 | 157 | 44 | inferred_complete_timeline |
| `Action_None` | 159 | 161 | 3 | inferred_complete_timeline |
| `Action_None` | 164 | 225 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 145 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 157 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 170 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 155 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 176 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 212 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–137 | 138 | 1 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–195 | 196 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 2–81 | 80 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 16–34 | 8 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 22–90 | 67 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 25–66 | 25 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 32–90 | 59 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 55–57 | 3 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 69–72 | 4 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 69–190 | 81 | 6 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 103–121 | 9 | 3 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 104–144 | 41 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 110–112 | 3 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 141–268 | 127 | 2 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 168–223 | 56 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 168–242 | 57 | 6 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 170–172 | 3 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 173–245 | 69 | 3 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 205–269 | 65 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 205–220 | 11 | 2 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 221–268 | 48 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 82 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 114: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [114-157] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-225] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-199] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-135] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-157] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-93] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-106] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-131] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-145] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-157] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-206] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-269] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-202] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-212] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-110] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-113] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-123] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-134] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-155] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-176] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-96] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-170] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-201] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-34] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-24] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-90] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-39] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-47] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-52] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-66] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-57] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-74] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-143] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-149] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-154] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-190] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-107] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-112] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-143] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-268] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-223] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-169] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-195] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-208] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-225] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-232] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-242] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-172] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-224] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-245] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-190] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-190] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-269] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-212] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-220] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-268] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>