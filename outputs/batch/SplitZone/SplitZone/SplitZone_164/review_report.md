# Play-Annotation-Generator Annotation Review — SplitZone_164

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_164`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `13` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `18` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `5` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 163 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 161 | START | 161 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `12` | 164 | START | 173 | 187 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `17` | `17` | 164 | START | 164 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `4` | `4` | 164 | START | 164 | 174 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `7` | 164 | START | 164 | 237 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `9` | 164 | START | 164 | 181 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | `13` | `13` | 168 | START | 168 | 194 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 172 | END | 161 | 172 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 176 | START | 176 | 187 |
| ✅ EXACT | `Action_BallCarry` | RB | `6` | `6` | 188 | START | 188 | 206 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 237 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 160 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 161 | 172 | 12 | inferred_complete_timeline |
| `Action_None` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 176 | 187 | 12 | inferred_complete_timeline |
| `Action_None` | 188 | 195 | 8 | inferred_complete_timeline |
| `Action_None` | 198 | 242 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 206 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 148 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 160 | 11 | inferred_complete_timeline |
| `Action_None` | 161 | 192 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_SplitBlock` | 168 | 194 | 27 | inferred_complete_timeline |
| `Action_SplitBlock` | 197 | 215 | 19 | inferred_complete_timeline |
| `Action_SplitBlock` | 219 | 224 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 275 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 199 | 36 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–280
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 174 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 200 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_None` | 238 | 280 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_BallSnap` | 161 | 172 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 187 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 222 | 32 | inferred_complete_timeline |
| `Action_None` | 252 | 259 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 181 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 204 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 237 | 74 | inferred_complete_timeline |
| `Action_None` | 238 | 238 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 217 | 57 | inferred_complete_timeline |
| `Action_None` | 223 | 225 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 160 | 54 | inferred_complete_timeline |
| `Action_None` | 161 | 176 | 16 | inferred_complete_timeline |
| `Action_None` | 182 | 184 | 3 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 199 | 3 | inferred_complete_timeline |
| `Action_None` | 201 | 227 | 27 | inferred_complete_timeline |
| `Action_None` | 231 | 248 | 18 | inferred_complete_timeline |
| `Action_None` | 254 | 255 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 93 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 160 | 61 | inferred_complete_timeline |
| `Action_None` | 161 | 177 | 17 | inferred_complete_timeline |
| `Action_None` | 180 | 187 | 8 | inferred_complete_timeline |
| `Action_None` | 191 | 199 | 9 | inferred_complete_timeline |
| `Action_None` | 201 | 205 | 5 | inferred_complete_timeline |
| `Action_None` | 210 | 226 | 17 | inferred_complete_timeline |
| `Action_None` | 230 | 236 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 160 | 53 | inferred_complete_timeline |
| `Action_None` | 161 | 222 | 62 | inferred_complete_timeline |
| `Action_None` | 226 | 230 | 5 | inferred_complete_timeline |
| `Action_None` | 232 | 234 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 184 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–378
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 307 | 147 | inferred_complete_timeline |
| `Action_None` | 309 | 360 | 52 | inferred_complete_timeline |
| `Action_None` | 370 | 375 | 6 | inferred_complete_timeline |
| `Action_None` | 377 | 378 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 197 | 37 | inferred_complete_timeline |
| `Action_None` | 207 | 261 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 256 | 96 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 118–250 | 120 | 5 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 135–233 | 80 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 215–389 | 169 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 215–248 | 23 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 229–232 | 4 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 236–251 | 16 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 261–266 | 5 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 265–271 | 7 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 269–389 | 106 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 303–304 | 2 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 309–389 | 80 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 311–389 | 75 | 3 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 317–389 | 68 | 2 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 320–389 | 67 | 2 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 387–389 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `13` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 82 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [161–172], lower_priority='Action_ZoneBlock' annotated_start=164, effective_Action_ZoneBlock_start=173.
- ⚠️ Action 'Action_None' range [161-197] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-261] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-256] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-307] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-360] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-375] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-217] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [164-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [179-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-280] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-148] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-192] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-206] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [164-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '7' starts at frame 238, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [238-238] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-136] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-195] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-242] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [164-181] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [186-204] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-176] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-227] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-248] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [173-187] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [191-222] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-259] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [168-194] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [197-215] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [219-224] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-93] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-160] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-199] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-205] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-226] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-236] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-99] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-222] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-184] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [164-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-275] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-189] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-204] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-226] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-250] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-207] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-233] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-304] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-372] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-248] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-251] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-271] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-321] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-370] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-335] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-324] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-351] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-361] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-347] for track '32' has 1 frames without a visible bounding box.
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