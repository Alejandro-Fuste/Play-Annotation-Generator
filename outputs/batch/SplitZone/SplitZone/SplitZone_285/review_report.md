# Play-Annotation-Generator Annotation Review — SplitZone_285

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_285`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 67
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 10
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `17` | `17` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `17` | `17` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `12` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `15` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 54 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 47 | START | 47 | 58 |
| ✅ EXACT | `Action_SplitBlock` | HB | `12` | `12` | 52 | START | 52 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `11` | `11` | 55 | START | 55 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 55 | START | 59 | 75 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `2` | 55 | START | 55 | 116 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `3` | `3` | 55 | START | 55 | 117 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `8` | 55 | START | 55 | 104 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 58 | END | 47 | 58 |
| ✅ EXACT | `Action_PressEdge` | RB | `17` | `17` | 66 | START | 66 | 76 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `14` | `14` | 76 | START | 76 | 106 |
| ✅ EXACT | `Action_Handoff` | RB | `17` | `17` | 77 | START | 77 | 86 |
| ✅ EXACT | `Action_BallCarry` | RB | `17` | `17` | 87 | START | 87 | 264 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 58 | 12 | inferred_complete_timeline |
| `Action_None` | 59 | 155 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PressEdge` | 66 | 76 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 77 | 86 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 87 | 264 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_SplitBlock` | 52 | 103 | 52 | inferred_complete_timeline |
| `Action_None` | 104 | 269 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 108 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 116 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 117 | 63 | inferred_complete_timeline |
| `Action_None` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_BallSnap` | 47 | 58 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 75 | 17 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 76 | 106 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 117 | 11 | inferred_complete_timeline |
| `Action_None` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 104 | 50 | inferred_complete_timeline |
| `Action_None` | 130 | 189 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 76 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 117 | 36 | inferred_complete_timeline |
| `Action_None` | 118 | 240 | 123 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 106 | 60 | inferred_complete_timeline |
| `Action_None` | 115 | 232 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 253 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 92 | 46 | inferred_complete_timeline |
| `Action_None` | 105 | 229 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 269 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 261 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 182 | 136 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_None` | 201 | 252 | 52 | inferred_complete_timeline |
| `Action_None` | 259 | 269 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 101 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 115 | 69 | inferred_complete_timeline |
| `Action_None` | 117 | 179 | 63 | inferred_complete_timeline |
| `Action_None` | 185 | 190 | 6 | inferred_complete_timeline |
| `Action_None` | 193 | 204 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 91 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 89–130 | 34 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 124–269 | 146 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 144–269 | 126 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 148–151 | 4 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 153–269 | 115 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 153–254 | 102 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 178–179 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 184–269 | 86 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 198–214 | 16 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 204–269 | 59 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 215–269 | 44 | 4 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 244–246 | 3 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 248–269 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 39 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [47–58], lower_priority='Action_ZoneBlock' annotated_start=55, effective_Action_ZoneBlock_start=59.
- ⚠️ Action 'Action_None' range [47-182] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-252] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-116] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-101] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-179] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-190] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-204] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-106] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-232] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-253] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-104] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-189] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-91] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-155] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-76] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-261] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-229] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [87-264] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-94] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-130] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-167] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-254] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-205] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-214] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-211] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-259] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '29' has 1 frames without a visible bounding box.
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

</details>