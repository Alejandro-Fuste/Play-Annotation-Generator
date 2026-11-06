# Play-Annotation-Generator Annotation Review — OutsideZoneRead_45

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_45`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `13` | `13` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `0` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `1` | `1` | 100 | START | 100 | 144 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `10` | `10` | 100 | START | 100 | 153 |
| ✅ EXACT | `Action_ZoneBlock` | C | `17` | `17` | 100 | START | 100 | 153 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 100 | START | 100 | 153 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `3` | `3` | 100 | START | 100 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `13` | `13` | 104 | START | 104 | 117 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `15` | `15` | 104 | START | 104 | 116 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `15` | 117 | START | 117 | 126 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 104 | 116 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 117 | 126 | 10 | inferred_complete_timeline |
| `Action_None` | 127 | 210 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 95 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 103 | 6 | inferred_complete_timeline |
| `Action_PressEdge` | 104 | 117 | 14 | inferred_complete_timeline |
| `Action_PressEdge` | 132 | 153 | 22 | inferred_complete_timeline |
| `Action_None` | 154 | 186 | 33 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 206 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 227 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 241 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 166 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 153 | 54 | inferred_complete_timeline |
| `Action_None` | 154 | 235 | 82 | inferred_complete_timeline |
| `Action_None` | 246 | 329 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 147 | 48 | inferred_complete_timeline |
| `Action_None` | 154 | 261 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 99 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 153 | 54 | inferred_complete_timeline |
| `Action_None` | 154 | 166 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 144 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 151 | 5 | inferred_complete_timeline |
| `Action_None` | 159 | 162 | 4 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 329 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 153 | 54 | inferred_complete_timeline |
| `Action_None` | 154 | 164 | 11 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 203 | 273 | 71 | inferred_complete_timeline |
| `Action_None` | 275 | 288 | 14 | inferred_complete_timeline |
| `Action_None` | 290 | 291 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 223 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 267 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 272 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 329 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 136 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 187 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 329 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 132 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 240 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 145 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 161 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 182 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 202 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 329 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–311
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 152 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 293 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 301 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 311 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 106–119 | 13 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 125–228 | 97 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 164–329 | 151 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 174–246 | 53 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 179–329 | 151 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 184–235 | 52 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 190–329 | 139 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 194–253 | 58 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 207–329 | 120 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 208–329 | 89 | 3 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 209–243 | 35 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 212–329 | 115 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 215–221 | 7 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 221–235 | 15 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 229–236 | 8 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 230–246 | 11 | 2 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 235–329 | 68 | 5 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 295–324 | 30 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 91 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-227] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-241] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-144] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-151] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-273] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-288] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-147] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-261] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-158] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-166] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-240] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-152] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-293] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-301] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-311] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-159] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-164] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-223] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-267] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-272] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-176] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-182] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-202] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-207] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-235] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-145] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-95] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [104-117] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [117-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-210] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-136] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-187] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-99] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-166] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-108] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-215] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-228] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-192] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-281] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-213] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-218] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-225] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-246] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-329] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-235] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-320] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-220] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-253] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-259] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-209] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-249] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-243] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-252] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-221] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-235] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-236] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-235] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-246] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-239] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-290] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-306] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-324] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-324] for track '35' has 1 frames without a visible bounding box.
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