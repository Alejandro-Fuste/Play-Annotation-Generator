# Play-Annotation-Generator Annotation Review — Hitch_60

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_60`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 185
- **Validation Warnings:** 190
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 168
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `16` | `16` |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `18` | `18` |
| ✅ EXACT | `Action_RunHitchRoute` | WR3 | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 2 | START | 2 | 6 |
| ✅ EXACT | `Action_PassBlock` | RT | `12` | `12` | 5 | START | 5 | 16 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `14` | 5 | START | 7 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `15` | `15` | 5 | START | 5 | 6 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `16` | `16` | 5 | START | 5 | 6 |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | `18` | `18` | 6 | END | 2 | 4 |
| ✅ EXACT | `Action_RunHitchRoute` | WR3 | `6` | `6` | 13 | START | 13 | 103 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `18` | `18` | 93 | START | 93 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `6` | `6` | 138 | START | 138 | 208 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 59 | 58 | inferred_complete_timeline |
| `Action_None` | 66 | 81 | 16 | inferred_complete_timeline |
| `Action_None` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_None` | 96 | 175 | 80 | inferred_complete_timeline |
| `Action_None` | 179 | 191 | 13 | inferred_complete_timeline |
| `Action_None` | 200 | 205 | 6 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 215 | 3 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 228 | 9 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 208 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 13 | 103 | 91 | inferred_complete_timeline |
| `Action_None` | 104 | 137 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 138 | 208 | 71 | inferred_complete_timeline |
| `Action_BallCarry` | 212 | 215 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 217 | 239 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 6 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 81 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 99 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 119 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 130 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 140 | 172 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 177 | 182 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 184 | 196 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 204 | 209 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 212 | 215 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 221 | 228 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 6 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 30 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 79 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 2 | 6 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 19 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 33 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 79 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 88 | 90 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 104 | 120 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 124 | 130 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 132 | 175 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 180 | 211 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 213 | 217 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 220 | 223 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–16
- **Visible Samples:** 17

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 16 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 9 | 8 | inferred_complete_timeline |
| `Action_None` | 95 | 164 | 70 | inferred_complete_timeline |
| `Action_None` | 170 | 194 | 25 | inferred_complete_timeline |
| `Action_None` | 197 | 208 | 12 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 239 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–7
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 7 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–4
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 4 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 82 | 81 | inferred_complete_timeline |
| `Action_None` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 232 | 231 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 34 | 33 | inferred_complete_timeline |
| `Action_None` | 36 | 44 | 9 | inferred_complete_timeline |
| `Action_None` | 46 | 98 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 156 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 215 | 214 | inferred_complete_timeline |
| `Action_None` | 219 | 239 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 2–239 | 180 | 12 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 46–239 | 174 | 7 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 48–239 | 186 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 55–145 | 62 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 65–158 | 64 | 6 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 67–192 | 94 | 6 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 74–239 | 64 | 9 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 97–145 | 49 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 98–113 | 16 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 105–130 | 22 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 114–239 | 74 | 6 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 123–222 | 16 | 7 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 127–239 | 59 | 11 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 143–172 | 27 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 164–239 | 57 | 5 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 169–239 | 67 | 3 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 191–193 | 3 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 205–208 | 4 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 222–239 | 13 | 3 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (14 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (15 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 147 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 70: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [2–6], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=7.
- ⚠️ Action 'Action_None' range [2-59] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-81] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-175] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-191] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-205] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-228] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-232] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-7] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-82] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [138-208] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [212-215] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-208] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-34] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-44] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-98] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-215] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-16] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-9] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-194] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-208] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-19] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-33] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-38] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-79] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [88-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [104-120] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [124-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [132-175] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [180-211] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [213-217] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [220-223] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-6] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-99] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-130] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [140-172] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [177-182] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [184-196] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [204-209] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [212-215] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [218-219] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [221-228] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-6] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-30] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-79] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-4] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [2-4] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-35] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [93-102] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-172] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-192] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-54] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-159] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-179] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-201] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-228] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-55] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-81] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-129] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-99] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-130] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-81] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-123] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-173] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-79] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-161] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-208] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-145] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-113] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-119] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-130] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-129] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-146] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-161] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-173] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-228] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-148] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-161] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-231] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-167] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-213] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-239] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-232] for track '33' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '36' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.

</details>