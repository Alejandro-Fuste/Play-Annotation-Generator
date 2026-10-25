# Play-Annotation-Generator Annotation Review — BootPass_49

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_49`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `18` | `18` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 19 | START | 19 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 19 | START | 19 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 19 | START | 19 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 19 | START | 19 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 19 | START | 19 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 19 | START | 19 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 19 | START | 19 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 19 | START | 19 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 19 | START | 19 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 19 | START | 19 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `8` | `Group` | 19 | START | 19 | 41 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 42 | START | 42 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `15` | `15` | 50 | START | 51 | 69 |
| ✅ EXACT | `Action_RunBlock` | RT | `16` | `16` | 50 | START | 50 | 214 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `18` | `18` | 50 | START | 50 | 56 |
| ✅ EXACT | `Action_RunBlock` | LT | `19` | `19` | 50 | START | 50 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `21` | `21` | 50 | START | 50 | 124 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 50 | END | 42 | 50 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `20` | `20` | 74 | START | 74 | 87 |
| ✅ EXACT | `Action_BootAway` | QB | `20` | `20` | 90 | START | 90 | 121 |
| ✅ EXACT | `Action_ThrowPass` | QB | `20` | `20` | 157 | START | 157 | 165 |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | WR2 | `1` | `1` | 235 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 19–197
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_SnapReceive` | 42 | 50 | 9 | inferred_complete_timeline |
| `Action_None` | 51 | 73 | 23 | inferred_complete_timeline |
| `Action_FakeHandoff` | 74 | 87 | 14 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_BootAway` | 90 | 121 | 32 | inferred_complete_timeline |
| `Action_None` | 122 | 156 | 35 | inferred_complete_timeline |
| `Action_ThrowPass` | 157 | 165 | 9 | inferred_complete_timeline |
| `Action_None` | 166 | 197 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 19–175
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_None` | 42 | 175 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 19–230
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_None` | 42 | 230 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 19–215
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 197 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 215 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 19–186
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_None` | 42 | 169 | 128 | inferred_complete_timeline |
| `Action_None` | 171 | 175 | 5 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 19–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_None` | 42 | 210 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 19–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 49 | 31 | inferred_complete_timeline |
| `Action_RunBlock` | 50 | 210 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 19–213
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 22 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 49 | 26 | inferred_complete_timeline |
| `Action_RunBlock` | 50 | 124 | 75 | inferred_complete_timeline |
| `Action_RunBlock` | 126 | 213 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 19–208
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_BallSnap` | 42 | 50 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 51 | 69 | 19 | inferred_complete_timeline |
| `Action_RunBlock` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 80 | 199 | 120 | inferred_complete_timeline |
| `Action_RunBlock` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 206 | 208 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 19–209
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 49 | 31 | inferred_complete_timeline |
| `Action_RunBlock` | 50 | 56 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 59 | 69 | 11 | inferred_complete_timeline |
| `Action_RunBlock` | 72 | 109 | 38 | inferred_complete_timeline |
| `Action_RunBlock` | 111 | 130 | 20 | inferred_complete_timeline |
| `Action_RunBlock` | 135 | 143 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 149 | 179 | 31 | inferred_complete_timeline |
| `Action_RunBlock` | 182 | 187 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 189 | 195 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 199 | 202 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 206 | 209 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 19–214
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 49 | 31 | inferred_complete_timeline |
| `Action_RunBlock` | 50 | 214 | 165 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 19–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_None` | 42 | 137 | 96 | inferred_complete_timeline |
| `Action_None` | 145 | 239 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 19–201
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_None` | 42 | 179 | 138 | inferred_complete_timeline |
| `Action_None` | 181 | 201 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 19–96
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_None` | 42 | 96 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 19–225
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_None` | 42 | 225 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 19–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_None` | 42 | 227 | 186 | inferred_complete_timeline |
| `Action_None` | 229 | 239 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 19–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_None` | 42 | 197 | 156 | inferred_complete_timeline |
| `Action_None` | 199 | 207 | 9 | inferred_complete_timeline |
| `Action_None` | 209 | 231 | 23 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 19–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_None` | 42 | 216 | 175 | inferred_complete_timeline |
| `Action_None` | 218 | 239 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 19–239
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_None` | 42 | 239 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 19–176
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_None` | 42 | 160 | 119 | inferred_complete_timeline |
| `Action_None` | 164 | 176 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 19–207
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_None` | 42 | 195 | 154 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 19–158
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_None` | 42 | 158 | 117 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 100–195 | 82 | 5 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 107–111 | 5 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 157–158 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 157–162 | 5 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 189–208 | 20 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 190–239 | 44 | 4 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 221–225 | 5 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 221–239 | 17 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (5 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (10 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (2 segments found)
- ❌ Missing segment for action `Action_SecureCatch` on target `1` (WR2)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_SecureCatch' for track '1' has invalid range: start=235, end=215. Clamping end to start.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [42–50], lower_priority='Action_RunBlock' annotated_start=50, effective_Action_RunBlock_start=51.
- ⚠️ Action 'Action_None' range [42-96] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-197] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-215] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-179] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-201] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-216] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-169] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-227] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-195] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-197] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-207] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-231] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-160] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-176] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [51-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [76-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [80-199] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [201-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [206-208] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [50-214] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-225] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [50-56] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [59-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [72-109] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [111-130] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [135-143] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [149-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [182-187] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [189-195] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [199-202] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [206-209] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [50-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-197] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-22] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [50-124] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [126-213] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-115] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-179] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-195] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-208] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-205] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-237] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-232] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '29' has 1 frames without a visible bounding box.
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

</details>