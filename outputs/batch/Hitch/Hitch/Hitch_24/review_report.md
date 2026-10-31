# Play-Annotation-Generator Annotation Review — Hitch_24

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_24`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 126
- **Validation Warnings:** 156
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 1
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 6
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 113
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `17` | `17` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `18` | `18` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LT | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_RunHitchRoute` | WR1 | offense | `0` | `0` |
| ⚠️ END CHANGED | `Action_SnapReceive` | LT | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | RB | offense | `16` | `16` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | WR1 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 19 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `17` | `17` | 20 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_PassBlock` | RT | `15` | `15` | 28 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `18` | `18` | 28 | START | 28 | 31 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LT | `19` | `19` | 28 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LG | `20` | `20` | 28 | START | N/A | N/A |
| ✅ EXACT | `Action_RunHitchRoute` | WR1 | `0` | `0` | 35 | START | 35 | 122 |
| ⚠️ END CHANGED | `Action_SnapReceive` | LT | `19` | `19` | 35 | END | 20 | 24 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | RB | `16` | `16` | 93 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | WR1 | `0` | `0` | 142 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–17
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 35 | 122 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–14
- **Visible Samples:** 15

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 239 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 239 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 19 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 24 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–10
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 31 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 48 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 107 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–17
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 239 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 239 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–4
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 26 | 7 | inferred_complete_timeline |
| `Action_None` | 41 | 47 | 7 | inferred_complete_timeline |
| `Action_None` | 63 | 67 | 5 | inferred_complete_timeline |
| `Action_None` | 69 | 72 | 4 | inferred_complete_timeline |
| `Action_None` | 82 | 88 | 7 | inferred_complete_timeline |
| `Action_None` | 93 | 99 | 7 | inferred_complete_timeline |
| `Action_None` | 111 | 184 | 74 | inferred_complete_timeline |
| `Action_None` | 187 | 235 | 49 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 67 | 48 | inferred_complete_timeline |
| `Action_None` | 71 | 82 | 12 | inferred_complete_timeline |
| `Action_None` | 90 | 239 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 45 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 239 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 93 | 74 | inferred_complete_timeline |
| `Action_None` | 97 | 99 | 3 | inferred_complete_timeline |
| `Action_None` | 101 | 196 | 96 | inferred_complete_timeline |
| `Action_None` | 200 | 217 | 18 | inferred_complete_timeline |
| `Action_None` | 221 | 225 | 5 | inferred_complete_timeline |
| `Action_None` | 228 | 232 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 239 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 127 | 108 | inferred_complete_timeline |
| `Action_None` | 129 | 143 | 15 | inferred_complete_timeline |
| `Action_None` | 145 | 239 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 20 | 22 | 3 | inferred_complete_timeline |
| `Action_None` | 95 | 188 | 94 | inferred_complete_timeline |
| `Action_None` | 190 | 202 | 13 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |
| `Action_None` | 215 | 218 | 4 | inferred_complete_timeline |
| `Action_None` | 220 | 225 | 6 | inferred_complete_timeline |
| `Action_None` | 228 | 234 | 7 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–51 | 52 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–14 | 15 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 41–239 | 199 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 80–173 | 68 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 83–84 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 88–239 | 112 | 5 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 93–239 | 135 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 98–239 | 139 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 100–137 | 9 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 105–239 | 135 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 105–219 | 45 | 6 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 110–228 | 101 | 5 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 110–170 | 53 | 2 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 112–239 | 105 | 9 | Undefined position; Undefined team |
| `34` | `36` | Position_Unknown | Team_Unknown | 130–239 | 108 | 3 | Undefined position; Undefined team |
| `35` | `37` | Position_Unknown | Team_Unknown | 153–227 | 38 | 4 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 165–166 | 2 | 1 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 178–179 | 2 | 1 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 185–187 | 3 | 1 | Undefined position; Undefined team |
| `39` | `43` | Position_Unknown | Team_Unknown | 186–198 | 9 | 2 | Undefined position; Undefined team |
| `40` | `44` | Position_Unknown | Team_Unknown | 188–210 | 12 | 2 | Undefined position; Undefined team |
| `41` | `45` | Position_Unknown | Team_Unknown | 191–235 | 37 | 4 | Undefined position; Undefined team |
| `42` | `47` | Position_Unknown | Team_Unknown | 194–196 | 3 | 1 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 208–209 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `17` (Position_Unknown)
- ❌ Missing segment for action `Action_PassBlock` on target `15` (RT)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (5 segments found)
- ❌ Missing segment for action `Action_PassBlock` on target `19` (LT)
- ❌ Missing segment for action `Action_PassBlock` on target `20` (LG)
- ❌ Missing segment for action `Action_ThrowPass` on target `16` (RB)
- ❌ Missing segment for action `Action_BallCarry` on target `0` (WR1)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 99 |
| Track-related warning | 8 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 33: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
- ⚠️ Row 34: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '0' has invalid range: start=142, end=122. Clamping end to start.
- ⚠️ Segment 'Action_PassBlock' for track '15' has invalid range: start=28, end=17. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '16' has invalid range: start=93, end=17. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=20, end=14. Clamping end to start.
- ⚠️ Segment 'Action_PassBlock' for track '19' has invalid range: start=28, end=19. Clamping end to start.
- ⚠️ Segment 'Action_PassBlock' for track '20' has invalid range: start=28, end=10. Clamping end to start.
- ⚠️ Action 'Action_RunHitchRoute' range [35-122] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-127] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-93] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-99] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-196] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-217] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-45] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-239] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-67] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-82] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-51] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 20, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [20-26] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-67] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-88] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-99] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-184] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-235] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-22] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-188] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-202] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-234] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-31] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-48] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [52-54] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [80-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [105-107] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [20-24] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-93] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-140] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-173] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-119] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-183] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-141] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-156] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-105] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-109] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-177] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-184] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-199] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-160] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-193] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-214] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-156] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-170] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-139] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-195] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-233] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-230] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-184] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-191] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-197] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-199] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-217] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-235] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.

</details>