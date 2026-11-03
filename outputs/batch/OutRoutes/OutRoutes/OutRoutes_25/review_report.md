# Play-Annotation-Generator Annotation Review — OutRoutes_25

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_25`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | TE | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 226 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 235 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `16` | `16` | 16 | START | 16 | 38 |
| ✅ EXACT | `Action_PassBlock` | LT | `18` | `18` | 16 | START | 16 | 229 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 16 | START | 16 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 16 | START | 16 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `21` | 16 | START | 16 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | TE | `0` | `0` | 21 | START | 21 | 145 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 21 | END | 21 | 21 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 21 | 1 | inferred_complete_timeline |
| `Action_None` | 22 | 116 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 96 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 177 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 226 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_RunOutRoute` | 21 | 145 | 125 | inferred_complete_timeline |
| `Action_RunOutRoute` | 148 | 216 | 69 | inferred_complete_timeline |
| `Action_RunOutRoute` | 219 | 253 | 35 | inferred_complete_timeline |
| `Action_RunOutRoute` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_RunOutRoute` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_RunOutRoute` | 264 | 265 | 2 | inferred_complete_timeline |
| `Action_RunOutRoute` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 229 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 178 | 163 | inferred_complete_timeline |
| `Action_PassBlock` | 186 | 229 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–42
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 38 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 42 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 62 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 65 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 57 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 84 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 174 | 88 | inferred_complete_timeline |
| `Action_PassBlock` | 177 | 229 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 244 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 57 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 246 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 169 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 244 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 269 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 269 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 269 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 269 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 72–267 | 196 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 76–113 | 38 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 95–97 | 3 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 124–250 | 127 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 143–254 | 100 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 154–265 | 89 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 181–232 | 20 | 6 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 225–239 | 15 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 225–240 | 16 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 228–229 | 2 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 228–232 | 5 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 230–236 | 7 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 230–238 | 9 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 230–234 | 5 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 230–241 | 12 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 244–259 | 16 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 248–249 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunOutRoute` and target `0` (7 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 65 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_RunOutRoute' range [21-145] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [148-216] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [219-253] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [258-259] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [261-262] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [264-265] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-226] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-231] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-244] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-235] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-152] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-133] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-169] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-244] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-57] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-246] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-214] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-116] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-259] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-42] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-96] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-100] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-177] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-229] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-178] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [186-229] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-62] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-65] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-57] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-84] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-174] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [177-229] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-267] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-113] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-97] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-250] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-229] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-254] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-160] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-229] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-265] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-183] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-194] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-211] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-218] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-232] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-239] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-240] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-232] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-236] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-238] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-234] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-241] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-259] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '38' has 1 frames without a visible bounding box.
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

</details>