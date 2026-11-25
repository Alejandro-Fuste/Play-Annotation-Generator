# Play-Annotation-Generator Annotation Review — InsideZoneRead_306

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_306`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 71
- **Validation Warnings:** 61
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `22` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `20` | `19` |
| ✅ EXACT | `Action_ReadDefender` | DE2 | defense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | DE2 | defense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE2 | defense | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `1` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 4 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `22` | `20` | 2 | START | 60 | 60 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `9` | 5 | START | 5 | 77 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `12` | 5 | START | 5 | 77 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `3` | 5 | START | 5 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `6` | `5` | 5 | START | 5 | 77 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `6` | 5 | START | 5 | 77 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `20` | `19` | 11 | END | 2 | 11 |
| ✅ EXACT | `Action_ReadDefender` | DE2 | `20` | `19` | 15 | START | 15 | 16 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | DE2 | `20` | `19` | 18 | START | 18 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE2 | `20` | `19` | 40 | START | 40 | 48 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 77 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 269 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 269 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 269 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_None` | 50 | 259 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 144 | 143 | inferred_complete_timeline |
| `Action_None` | 146 | 155 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 77 | 73 | inferred_complete_timeline |
| `Action_None` | 78 | 269 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 77 | 73 | inferred_complete_timeline |
| `Action_None` | 78 | 92 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 77 | 73 | inferred_complete_timeline |
| `Action_None` | 78 | 120 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 77 | 73 | inferred_complete_timeline |
| `Action_None` | 78 | 186 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 77 | 73 | inferred_complete_timeline |
| `Action_None` | 78 | 126 | 49 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 228 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 11 | 10 | inferred_complete_timeline |
| `Action_None` | 12 | 14 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 15 | 16 | 2 | inferred_complete_timeline |
| `Action_Keep` | 18 | 21 | 4 | inferred_complete_timeline |
| `Action_Keep` | 33 | 39 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 40 | 48 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 51 | 216 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 209 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 186 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 161 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 61 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 221 | 220 | inferred_complete_timeline |
| `Action_None` | 239 | 243 | 5 | inferred_complete_timeline |
| `Action_None` | 245 | 269 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_None` | 75 | 269 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 247 | 246 | inferred_complete_timeline |
| `Action_None` | 250 | 253 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 87 | 86 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `22` | Position_Unknown | Team_Unknown | 60–269 | 210 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 116–269 | 154 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 122–269 | 143 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 154–156 | 3 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 165–259 | 95 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 175–225 | 27 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 228–237 | 10 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 235–242 | 7 | 2 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `22` (Position_Unknown): Annotated start 2 != Inferred start 60
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '20' has invalid range: start=60, end=11. Clamping end to start.
- ⚠️ Action 'Action_None' range [2-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-61] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-247] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-253] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-92] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-87] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-40] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-186] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-144] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-155] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-269] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-221] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-228] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-48] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-259] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-161] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-209] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-186] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-14] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [15-16] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [18-21] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [40-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [51-216] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-228] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-259] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-195] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-237] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-242] for track '28' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_306'; source metadata written as null.

</details>