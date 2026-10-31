# Play-Annotation-Generator Annotation Review — Hitch_26

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_26`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `4` | `4` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `4` | `4` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunHitchRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `10` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `12` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 30 |
| ✅ EXACT | `Action_BallSnap` | C | `4` | `4` | 25 | START | 25 | 39 |
| ✅ EXACT | `Action_PassBlock` | LG | `16` | `16` | 31 | START | 31 | 103 |
| ✅ EXACT | `Action_PassBlock` | RT | `20` | `20` | 31 | START | 31 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 31 | START | 31 | 98 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `4` | `4` | 31 | START | 40 | 83 |
| ✅ EXACT | `Action_PassBlock` | LT | `7` | `7` | 31 | START | 31 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunHitchRoute` | WR2 | `1` | `1` | 33 | START | 33 | 33 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 39 | END | 25 | 39 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 83 | START | 83 | 94 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `1` | `1` | 131 | START | 131 | 210 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 39 | 15 | inferred_complete_timeline |
| `Action_None` | 40 | 82 | 43 | inferred_complete_timeline |
| `Action_ThrowPass` | 83 | 94 | 12 | inferred_complete_timeline |
| `Action_None` | 95 | 210 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 39 | 15 | inferred_complete_timeline |
| `Action_None` | 46 | 210 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 210 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 36 | 38 | 3 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 40 | 89 | 50 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 93 | 126 | 34 | inferred_complete_timeline |
| `Action_None` | 127 | 130 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 131 | 210 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 120 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 90 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 112 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 103 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_BallSnap` | 25 | 39 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 83 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 30 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 98 | 68 | inferred_complete_timeline |
| `Action_PassBlock` | 104 | 109 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 113 | 152 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 159 | 210 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 71 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 210 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 171 | 147 | inferred_complete_timeline |
| `Action_None` | 174 | 177 | 4 | inferred_complete_timeline |
| `Action_None` | 180 | 199 | 20 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 210 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 179 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 45 | 21 | inferred_complete_timeline |
| `Action_None` | 73 | 191 | 119 | inferred_complete_timeline |
| `Action_None` | 195 | 197 | 3 | inferred_complete_timeline |
| `Action_None` | 199 | 210 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 210 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 210 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 41 | 17 | inferred_complete_timeline |
| `Action_None` | 43 | 176 | 134 | inferred_complete_timeline |
| `Action_None` | 181 | 210 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 91 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 47 | 23 | inferred_complete_timeline |
| `Action_None` | 49 | 55 | 7 | inferred_complete_timeline |
| `Action_None` | 93 | 101 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 36 | 12 | inferred_complete_timeline |
| `Action_None` | 38 | 74 | 37 | inferred_complete_timeline |
| `Action_None` | 77 | 145 | 69 | inferred_complete_timeline |
| `Action_None` | 147 | 210 | 64 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–17 | 16 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 43–210 | 162 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 56–106 | 49 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 61–210 | 149 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 96–114 | 7 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 109–210 | 102 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 112–210 | 99 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 114–210 | 96 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 124–210 | 74 | 5 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 129–210 | 76 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 133–134 | 2 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 135–210 | 76 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 158–208 | 38 | 3 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 195–210 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `4` (C): Annotated start 31 != Inferred start 40
- ⚠️ Ambiguous match for action `Action_RunHitchRoute` and target `1` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [25–39], lower_priority='Action_PassBlock' annotated_start=31, effective_Action_PassBlock_start=40.
- ⚠️ Action 'Action_None' range [25-210] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunHitchRoute' for track '1' starts at frame 33, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_RunHitchRoute' range [33-33] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunHitchRoute' range [36-38] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunHitchRoute' range [40-89] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunHitchRoute' range [93-126] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [131-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-199] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-83] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-210] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-41] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-176] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-112] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-210] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-47] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-55] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-90] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-179] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-45] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-191] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-145] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-210] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-91] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-39] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-71] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-98] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [104-109] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [113-152] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [159-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-9] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-17] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-70] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-110] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-120] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-59] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-73] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-106] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-169] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-119] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-137] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-148] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-174] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-150] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-166] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-208] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '35' has 1 frames without a visible bounding box.
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

</details>