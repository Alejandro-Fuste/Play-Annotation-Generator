# Play-Annotation-Generator Annotation Review — Hitch_70

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_70`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_RunHitchRoute` | WR2 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 8 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 6 | START | 6 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `14` | 9 | START | 25 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 9 | START | 9 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 9 | START | 9 | 137 |
| ✅ EXACT | `Action_PassBlock` | RT | `21` | `21` | 9 | START | 9 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `4` | `4` | 9 | START | 9 | 54 |
| ✅ EXACT | `Action_RunHitchRoute` | WR2 | `0` | `0` | 24 | START | 24 | 96 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 24 | END | 6 | 24 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 87 | START | 87 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `0` | `0` | 141 | START | 141 | 215 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_SnapReceive` | 6 | 24 | 19 | inferred_complete_timeline |
| `Action_None` | 25 | 86 | 62 | inferred_complete_timeline |
| `Action_ThrowPass` | 87 | 97 | 11 | inferred_complete_timeline |
| `Action_None` | 98 | 239 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 239 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 239 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 24 | 96 | 73 | inferred_complete_timeline |
| `Action_None` | 97 | 140 | 44 | inferred_complete_timeline |
| `Action_BallCarry` | 141 | 215 | 75 | inferred_complete_timeline |
| `Action_BallCarry` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 222 | 224 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 239 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–20
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 20 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 54 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 64 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 239 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 37 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 121 | 83 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 139 | 239 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 6 | 24 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 69 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 107 | 108 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 137 | 129 | inferred_complete_timeline |
| `Action_PassBlock` | 139 | 239 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 239 | 231 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 89 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 50 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 160 | 155 | inferred_complete_timeline |
| `Action_None` | 164 | 175 | 12 | inferred_complete_timeline |
| `Action_None` | 178 | 191 | 14 | inferred_complete_timeline |
| `Action_None` | 193 | 239 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 137 | 132 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 160 | 5 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 180 | 14 | inferred_complete_timeline |
| `Action_None` | 183 | 232 | 50 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 239 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 188 | 183 | inferred_complete_timeline |
| `Action_None` | 218 | 239 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 153 | 148 | inferred_complete_timeline |
| `Action_None` | 156 | 190 | 35 | inferred_complete_timeline |
| `Action_None` | 195 | 239 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 227 | 222 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 54 | 49 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_None` | 63 | 124 | 62 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 175 | 40 | inferred_complete_timeline |
| `Action_None` | 180 | 200 | 21 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 218 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 195 | 190 | inferred_complete_timeline |
| `Action_None` | 197 | 228 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 19–20 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 27–239 | 211 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 72–145 | 51 | 5 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 83–239 | 156 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 119–239 | 120 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 146–151 | 6 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 148–153 | 6 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 149–239 | 88 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 159–228 | 45 | 5 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 181–191 | 11 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 196–198 | 3 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 218–239 | 9 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [6–24], lower_priority='Action_PassBlock' annotated_start=9, effective_Action_PassBlock_start=25.
- ⚠️ Action 'Action_BallCarry' range [141-215] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [217-218] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [222-224] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-227] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-54] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-64] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-137] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-232] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-195] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-228] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-89] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-153] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-190] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-50] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-218] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-239] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-160] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-175] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-191] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-54] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-124] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-200] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-69] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [94-96] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [107-108] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-188] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-20] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-37] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-121] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [135-136] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-137] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-20] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-30] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-84] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-124] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-136] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-153] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-187] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-178] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-208] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-219] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-191] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '34' has 1 frames without a visible bounding box.
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

</details>