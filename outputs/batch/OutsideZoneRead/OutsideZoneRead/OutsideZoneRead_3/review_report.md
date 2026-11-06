# Play-Annotation-Generator Annotation Review — OutsideZoneRead_3

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_3`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `6` | `6` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_Handoff` | CB1 | defense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 207 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `19` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `11` | 52 | START | 52 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `20` | 52 | START | 52 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 52 | START | 52 | 55 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `4` | 52 | START | 52 | 97 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `8` | 52 | START | 52 | 84 |
| ✅ EXACT | `Action_PressEdge` | RB | `6` | `6` | 63 | START | 63 | 110 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `13` | `13` | 66 | START | 66 | 88 |
| ✅ EXACT | `Action_Handoff` | CB1 | `5` | `5` | 94 | START | 94 | 98 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 66 | 88 | 23 | inferred_complete_timeline |
| `Action_None` | 89 | 251 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PressEdge` | 63 | 110 | 48 | inferred_complete_timeline |
| `Action_None` | 118 | 140 | 23 | inferred_complete_timeline |
| `Action_None` | 143 | 165 | 23 | inferred_complete_timeline |
| `Action_None` | 167 | 171 | 5 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 207 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 299 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 167 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 84 | 33 | inferred_complete_timeline |
| `Action_None` | 116 | 256 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 97 | 46 | inferred_complete_timeline |
| `Action_None` | 98 | 299 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 64 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 97 | 15 | inferred_complete_timeline |
| `Action_None` | 98 | 175 | 78 | inferred_complete_timeline |
| `Action_None` | 178 | 281 | 104 | inferred_complete_timeline |
| `Action_None` | 283 | 299 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 55 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 74 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 83 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 97 | 11 | inferred_complete_timeline |
| `Action_None` | 98 | 140 | 43 | inferred_complete_timeline |
| `Action_None` | 144 | 289 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 67 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 97 | 24 | inferred_complete_timeline |
| `Action_None` | 98 | 98 | 1 | inferred_complete_timeline |
| `Action_None` | 105 | 299 | 195 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 125 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 133 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 299 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 133 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 165 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 110 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 141 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 198 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_Handoff` | 94 | 98 | 5 | inferred_complete_timeline |
| `Action_None` | 99 | 299 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 299 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 299 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 275 | 160 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 299 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 81–82 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 92–155 | 57 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 131–279 | 133 | 9 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 148–299 | 149 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 185–209 | 25 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 185–299 | 97 | 8 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 187–299 | 107 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 203–209 | 7 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 208–299 | 89 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 217–299 | 83 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 225–226 | 2 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 229–299 | 65 | 4 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 285–299 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 80 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-207] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-166] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [63-110] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-140] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-84] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-256] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-64] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-281] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-165] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-251] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-198] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-204] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-275] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-113] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-133] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-110] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-167] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-67] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '20' starts at frame 98, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [98-98] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-55] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-74] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-83] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-140] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-289] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-107] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-155] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-146] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-209] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-215] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-219] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-240] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-255] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-264] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-279] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-215] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-229] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-209] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-244] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-251] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-261] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-268] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-277] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-286] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-296] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-192] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-209] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-295] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-241] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-265] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-271] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-299] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-269] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-293] for track '35' has 1 frames without a visible bounding box.
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