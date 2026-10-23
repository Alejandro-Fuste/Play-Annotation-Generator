# Play-Annotation-Generator Annotation Review — WRSlowScreens_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `WRSlowScreens_1`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_WRSlowScreens`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | offense | `22` | `22` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReleaseToScreen` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_TurnToQuarterback` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR1 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 18 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `22` | 19 | START | 19 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `17` | `17` | 22 | START | 22 | 87 |
| ✅ EXACT | `Action_PassBlock` | LG | `19` | `19` | 22 | START | 22 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 22 | START | 22 | 35 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | `22` | `22` | 22 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 34 | END | 19 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReleaseToScreen` | LG | `19` | `19` | 55 | START | 55 | 125 |
| ✅ EXACT | `Action_TurnToQuarterback` | WR1 | `0` | `0` | 58 | START | 58 | 109 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `16` | `16` | 79 | START | 79 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR1 | `0` | `0` | 110 | START | 110 | 218 |

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
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 34 | 16 | inferred_complete_timeline |
| `Action_None` | 35 | 78 | 44 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 79 | 88 | 10 | inferred_complete_timeline |
| `Action_None` | 89 | 269 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 123 | 105 | inferred_complete_timeline |
| `Action_None` | 133 | 179 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_TurnToQuarterback` | 58 | 109 | 52 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 110 | 218 | 109 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 220 | 241 | 22 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 246 | 269 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 51 | 33 | inferred_complete_timeline |
| `Action_None` | 53 | 89 | 37 | inferred_complete_timeline |
| `Action_None` | 94 | 218 | 125 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 244 | 226 | inferred_complete_timeline |
| `Action_None` | 246 | 269 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 56 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 54 | 33 | inferred_complete_timeline |
| `Action_ReleaseToScreen` | 55 | 125 | 71 | inferred_complete_timeline |
| `Action_ReleaseToScreen` | 128 | 136 | 9 | inferred_complete_timeline |
| `Action_ReleaseToScreen` | 138 | 269 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–19
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 19 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 35 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 47 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 87 | 66 | inferred_complete_timeline |
| `Action_PassBlock` | 173 | 174 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 184 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 117 | 99 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 124 | 269 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 221 | 203 | inferred_complete_timeline |
| `Action_None` | 226 | 227 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 236 | 218 | inferred_complete_timeline |
| `Action_None` | 241 | 269 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 224 | 206 | inferred_complete_timeline |
| `Action_None` | 226 | 269 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 231 | 213 | inferred_complete_timeline |
| `Action_None` | 233 | 269 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 82 | 64 | inferred_complete_timeline |
| `Action_None` | 89 | 269 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 269 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 269 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 89 | 71 | inferred_complete_timeline |
| `Action_None` | 97 | 99 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–269 | 240 | 8 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–262 | 261 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–269 | 255 | 6 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 23–103 | 45 | 6 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 51–269 | 219 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 58–269 | 212 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 81–88 | 8 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 87–269 | 183 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 104–197 | 94 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 110–111 | 2 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 116–135 | 15 | 3 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 121–122 | 2 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 157–159 | 3 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 178–179 | 2 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 187–269 | 83 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 188–269 | 74 | 3 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 190–269 | 80 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 207–209 | 3 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 240–245 | 4 | 2 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 248–254 | 7 | 1 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 261–269 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ❌ Missing segment for action `Action_PassBlock` on target `22` (C)
- ⚠️ Ambiguous match for action `Action_ReleaseToScreen` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunAfterCatch` and target `0` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 4: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 4: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_PassBlock' for track '22' has invalid range: start=22, end=19. Clamping end to start.
- ⚠️ Action 'Action_RunAfterCatch' range [110-218] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [220-241] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-236] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-89] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-99] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-244] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-51] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-89] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-218] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-56] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-231] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-224] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-221] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-82] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-141] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-92] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-262] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-184] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-117] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-87] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [173-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-179] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-54] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReleaseToScreen' range [55-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReleaseToScreen' range [128-136] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-35] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-15] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-50] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-130] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' for track '22' starts at frame 19, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallSnap' range [19-19] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-30] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-59] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-78] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-88] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-88] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-125] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-269] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-216] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-254] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

</details>