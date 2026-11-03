# Play-Annotation-Generator Annotation Review — PuntBlock_15

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_15`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 146
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 101
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `18` | `18` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `9` | `Group` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `13` | `13` |
| ✅ EXACT | `Action_BlockPunt` | Right_Edge_Rusher1 | defense | `3` | `3` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Position_Unknown | Team_Unknown | `48` | `33` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `18` | `18` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `0` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `10` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `13` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `15` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `16` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `18` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `4` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `6` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `9` | `Group` | 0 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Punter | `13` | `13` | 24 | END | 24 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `13` | `13` | 48 | START | 48 | 71 |
| ✅ EXACT | `Action_BlockPunt` | Right_Edge_Rusher1 | `3` | `3` | 59 | START | 59 | 63 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Position_Unknown | `48` | `33` | 164 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 228 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 53 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 91 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_LongSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_LongSnap` | 20 | 47 | 28 | inferred_complete_timeline |
| `Action_None` | 48 | 114 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 80 | 256 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 55 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 24 | 1 | inferred_complete_timeline |
| `Action_None` | 25 | 47 | 23 | inferred_complete_timeline |
| `Action_PuntBall` | 48 | 71 | 24 | inferred_complete_timeline |
| `Action_PuntBall` | 76 | 128 | 53 | inferred_complete_timeline |
| `Action_PuntBall` | 133 | 138 | 6 | inferred_complete_timeline |
| `Action_PuntBall` | 141 | 146 | 6 | inferred_complete_timeline |
| `Action_PuntBall` | 150 | 252 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_None` | 245 | 329 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 122 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 97 | 329 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 66 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 23 | 27 | 5 | inferred_complete_timeline |
| `Action_None` | 29 | 80 | 52 | inferred_complete_timeline |
| `Action_None` | 86 | 93 | 8 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_None` | 140 | 144 | 5 | inferred_complete_timeline |
| `Action_None` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 175 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 10 | 15 | 6 | inferred_complete_timeline |
| `Action_None` | 17 | 25 | 9 | inferred_complete_timeline |
| `Action_None` | 30 | 136 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 38 | 41 | 4 | inferred_complete_timeline |
| `Action_None` | 50 | 69 | 20 | inferred_complete_timeline |
| `Action_None` | 72 | 257 | 186 | inferred_complete_timeline |
| `Action_None` | 259 | 267 | 9 | inferred_complete_timeline |
| `Action_None` | 269 | 329 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 72 | 99 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 84 | 329 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 109 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_BlockPunt` | 59 | 63 | 5 | inferred_complete_timeline |
| `Action_None` | 64 | 70 | 7 | inferred_complete_timeline |
| `Action_None` | 72 | 329 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–218 | 207 | 5 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 4–7 | 4 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 11–82 | 69 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 30–53 | 11 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 31–53 | 13 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 36–329 | 292 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 55–120 | 8 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 62–265 | 203 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 69–70 | 2 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 72–329 | 254 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 79–269 | 191 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 85–200 | 116 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 95–102 | 8 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 98–101 | 4 | 1 | Undefined position; Undefined team |
| `34` | `52` | Position_Unknown | Team_Unknown | 104–105 | 2 | 1 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 105–132 | 10 | 4 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 117–172 | 51 | 4 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 118–142 | 13 | 3 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 125–156 | 24 | 4 | Undefined position; Undefined team |
| `39` | `64` | Position_Unknown | Team_Unknown | 182–215 | 4 | 2 | Undefined position; Undefined team |
| `40` | `66` | Position_Unknown | Team_Unknown | 187–192 | 5 | 2 | Undefined position; Undefined team |
| `41` | `74` | Position_Unknown | Team_Unknown | 231–232 | 2 | 1 | Undefined position; Undefined team |
| `42` | `77` | Position_Unknown | Team_Unknown | 238–250 | 12 | 2 | Undefined position; Undefined team |
| `43` | `78` | Position_Unknown | Team_Unknown | 247–248 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PuntBall` and target `13` (5 segments found)
- ❌ Missing segment for action `Action_SecureRecovery` on target `33` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 95 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureRecovery' for track '33' has invalid range: start=164, end=101. Clamping end to start.
- ⚠️ Action 'Action_None' range [0-122] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-30] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-41] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-69] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-257] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-267] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' range [59-63] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-70] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-80] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-228] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-109] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-14] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-53] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-55] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-20] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-27] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-80] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-93] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-125] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-66] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-99] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [48-71] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [76-128] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [133-138] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [141-146] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [150-252] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-66] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-243] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-73] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-256] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [0-15] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-14] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-53] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-62] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-218] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-6] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-15] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-25] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-7] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-62] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-82] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-37] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-33] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-41] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-67] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-60] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-74] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-265] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-235] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-269] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-200] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-102] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-101] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-143] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-166] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-122] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-146] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-246] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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