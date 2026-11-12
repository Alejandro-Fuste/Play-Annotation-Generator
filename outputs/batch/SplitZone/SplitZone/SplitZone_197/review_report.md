# Play-Annotation-Generator Annotation Review — SplitZone_197

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_197`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SplitBlock` | TE1 | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 11 | START | 12 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 11 | START | 12 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 11 | START | 12 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 11 | START | 12 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 11 | START | 12 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 11 | START | 12 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 11 | START | 12 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 11 | START | 12 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 11 | START | 12 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 11 | START | 12 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 11 | START | 12 | 127 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 114 | START | 114 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `17` | `17` | 117 | START | 117 | 216 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `18` | 117 | START | 117 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 117 | START | 131 | 163 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 117 | START | 117 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 117 | START | 117 | 141 |
| ✅ EXACT | `Action_SplitBlock` | TE1 | `6` | `6` | 128 | START | 128 | 223 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 130 | END | 114 | 130 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `15` | 141 | START | 141 | 147 |
| ✅ EXACT | `Action_BallCarry` | RB | `3` | `3` | 148 | START | 148 | 168 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 223 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 113 | 102 | inferred_complete_timeline |
| `Action_SnapReceive` | 114 | 130 | 17 | inferred_complete_timeline |
| `Action_None` | 131 | 140 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 141 | 147 | 7 | inferred_complete_timeline |
| `Action_None` | 148 | 299 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 12–168
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 147 | 136 | inferred_complete_timeline |
| `Action_BallCarry` | 148 | 168 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 12–207
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 113 | 102 | inferred_complete_timeline |
| `Action_None` | 114 | 181 | 68 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 113 | 102 | inferred_complete_timeline |
| `Action_None` | 114 | 238 | 125 | inferred_complete_timeline |
| `Action_None` | 241 | 299 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 127 | 116 | inferred_complete_timeline |
| `Action_SplitBlock` | 128 | 223 | 96 | inferred_complete_timeline |
| `Action_None` | 224 | 299 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 113 | 102 | inferred_complete_timeline |
| `Action_None` | 114 | 153 | 40 | inferred_complete_timeline |
| `Action_None` | 155 | 246 | 92 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_None` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_None` | 261 | 299 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 12–178
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 116 | 105 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 148 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 165 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 178 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 116 | 105 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 141 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 223 | 79 | inferred_complete_timeline |
| `Action_None` | 224 | 259 | 36 | inferred_complete_timeline |
| `Action_None` | 284 | 287 | 4 | inferred_complete_timeline |
| `Action_None` | 291 | 299 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 12–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 113 | 102 | inferred_complete_timeline |
| `Action_BallSnap` | 114 | 130 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 131 | 163 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 204 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 223 | 17 | inferred_complete_timeline |
| `Action_None` | 224 | 239 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 12–200
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 116 | 105 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 142 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 177 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 197 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 199 | 200 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 116 | 105 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 216 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 223 | 223 | 1 | inferred_complete_timeline |
| `Action_None` | 224 | 299 | 76 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 113 | 102 | inferred_complete_timeline |
| `Action_None` | 114 | 145 | 32 | inferred_complete_timeline |
| `Action_None` | 147 | 299 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 12–172
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 113 | 102 | inferred_complete_timeline |
| `Action_None` | 114 | 167 | 54 | inferred_complete_timeline |
| `Action_None` | 169 | 172 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 113 | 102 | inferred_complete_timeline |
| `Action_None` | 114 | 299 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 113 | 102 | inferred_complete_timeline |
| `Action_None` | 114 | 162 | 49 | inferred_complete_timeline |
| `Action_None` | 167 | 237 | 71 | inferred_complete_timeline |
| `Action_None` | 239 | 299 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 113 | 102 | inferred_complete_timeline |
| `Action_None` | 114 | 207 | 94 | inferred_complete_timeline |
| `Action_None` | 212 | 235 | 24 | inferred_complete_timeline |
| `Action_None` | 239 | 266 | 28 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |
| `Action_None` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_None` | 275 | 281 | 7 | inferred_complete_timeline |
| `Action_None` | 285 | 299 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 113 | 102 | inferred_complete_timeline |
| `Action_None` | 114 | 299 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 113 | 102 | inferred_complete_timeline |
| `Action_None` | 114 | 299 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 113 | 102 | inferred_complete_timeline |
| `Action_None` | 114 | 299 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 12–292
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 113 | 102 | inferred_complete_timeline |
| `Action_None` | 114 | 258 | 145 | inferred_complete_timeline |
| `Action_None` | 265 | 292 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 113 | 102 | inferred_complete_timeline |
| `Action_None` | 114 | 257 | 144 | inferred_complete_timeline |
| `Action_None` | 260 | 299 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 12–273
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 113 | 102 | inferred_complete_timeline |
| `Action_None` | 114 | 221 | 108 | inferred_complete_timeline |
| `Action_None` | 226 | 233 | 8 | inferred_complete_timeline |
| `Action_None` | 240 | 244 | 5 | inferred_complete_timeline |
| `Action_None` | 249 | 253 | 5 | inferred_complete_timeline |
| `Action_None` | 272 | 273 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 175–299 | 125 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 186–299 | 104 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 189–299 | 109 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 212–299 | 88 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 227–248 | 21 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 253–299 | 47 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 275–299 | 11 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (RT) duration 107 frames exceeds threshold 90 frames [start=117, end=223].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (C) duration 107 frames exceeds threshold 90 frames [start=117, end=223].
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [114–130], lower_priority='Action_ZoneBlock' annotated_start=117, effective_Action_ZoneBlock_start=131.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 107 frames exceeds threshold 90 frames [start=117, end=223].
- ⚠️ Action 'Action_None' range [114-167] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-238] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-181] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [148-168] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-153] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-246] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-162] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-237] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-299] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-145] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-258] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-292] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-221] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-233] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-244] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-253] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-257] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-207] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-266] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-281] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-216] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-148] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [150-165] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-178] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [131-163] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-204] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-142] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [145-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [181-197] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [199-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-141] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [145-223] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-259] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-287] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-202] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-254] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-276] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-248] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-283] for track '28' has 1 frames without a visible bounding box.
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

</details>