# Play-Annotation-Generator Annotation Review — BootPass_62

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_62`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 143
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `0` | `0` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `16` | `16` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | LB1 | defense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | RB1 | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 16 | START | 16 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `10` | `Group` | 16 | START | 16 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 16 | START | 16 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 16 | START | 16 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 16 | START | 16 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `14` | `Group` | 16 | START | 16 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 16 | START | 16 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 16 | START | 16 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 16 | START | 16 | 41 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 42 | START | 42 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `0` | `0` | 50 | START | 50 | 83 |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `12` | `12` | 50 | START | 59 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `13` | `13` | 50 | START | 51 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `4` | `4` | 50 | START | 50 | 82 |
| ✅ EXACT | `Action_RunBlock` | RG | `5` | `5` | 50 | START | 50 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `11` | `11` | 58 | END | 42 | 55 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `11` | `11` | 65 | START | 65 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | QB | `11` | `11` | 81 | START | 81 | 82 |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `16` | `16` | 81 | START | 81 | 124 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | LB1 | `9` | `9` | 180 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | RB1 | `14` | `14` | 203 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 16–179
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 41 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 42 | 55 | 14 | inferred_complete_timeline |
| `Action_SnapReceive` | 57 | 58 | 2 | inferred_complete_timeline |
| `Action_None` | 60 | 64 | 5 | inferred_complete_timeline |
| `Action_FakeHandoff` | 65 | 80 | 16 | inferred_complete_timeline |
| `Action_BootAway` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_BootAway` | 87 | 121 | 35 | inferred_complete_timeline |
| `Action_None` | 122 | 132 | 11 | inferred_complete_timeline |
| `Action_None` | 151 | 179 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 16–149
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 44 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 57 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 69 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 86 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 101 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 149 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 16–70
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 41 | 26 | inferred_complete_timeline |
| `Action_None` | 42 | 70 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 16–93
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 41 | 26 | inferred_complete_timeline |
| `Action_None` | 42 | 63 | 22 | inferred_complete_timeline |
| `Action_None` | 84 | 93 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 16–108
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 49 | 34 | inferred_complete_timeline |
| `Action_RunBlock` | 50 | 82 | 33 | inferred_complete_timeline |
| `Action_RunBlock` | 86 | 90 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 100 | 108 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 16–89
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 48 | 33 | inferred_complete_timeline |
| `Action_RunBlock` | 51 | 54 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 56 | 89 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 16–121
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 41 | 26 | inferred_complete_timeline |
| `Action_BallSnap` | 42 | 58 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 59 | 121 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 16–125
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 49 | 34 | inferred_complete_timeline |
| `Action_RunBlock` | 50 | 125 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 16–99
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 49 | 34 | inferred_complete_timeline |
| `Action_RunBlock` | 50 | 83 | 34 | inferred_complete_timeline |
| `Action_RunBlock` | 85 | 88 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 93 | 99 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 16–105
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 41 | 26 | inferred_complete_timeline |
| `Action_None` | 42 | 84 | 43 | inferred_complete_timeline |
| `Action_None` | 92 | 105 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 16–194
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 41 | 26 | inferred_complete_timeline |
| `Action_None` | 42 | 194 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 16–115
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 41 | 26 | inferred_complete_timeline |
| `Action_None` | 42 | 115 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 16–158
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 41 | 26 | inferred_complete_timeline |
| `Action_None` | 42 | 134 | 93 | inferred_complete_timeline |
| `Action_None` | 138 | 158 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 16–117
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 117 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 16–329
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 41 | 26 | inferred_complete_timeline |
| `Action_None` | 42 | 77 | 36 | inferred_complete_timeline |
| `Action_None` | 79 | 111 | 33 | inferred_complete_timeline |
| `Action_None` | 113 | 315 | 203 | inferred_complete_timeline |
| `Action_None` | 318 | 319 | 2 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 72–101 | 29 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 80–329 | 250 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 102–117 | 11 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 109–189 | 81 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 114–170 | 56 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 162–329 | 153 | 5 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 179–329 | 138 | 5 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 184–309 | 121 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 194–268 | 75 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 200–252 | 47 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 214–215 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 222–263 | 40 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 228–241 | 14 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 231–329 | 95 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 232–247 | 16 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 233–251 | 19 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 235–329 | 94 | 2 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 235–249 | 7 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 244–268 | 25 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 246–329 | 84 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 248–321 | 74 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 251–329 | 79 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 256–305 | 50 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 268–329 | 58 | 3 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 272–329 | 58 | 1 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 277–329 | 53 | 1 | Undefined position; Undefined team |
| `41` | `46` | Position_Unknown | Team_Unknown | 294–329 | 34 | 2 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 319–329 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `0` (3 segments found)
- ⚠️ `Action_RunBlock` for actor_track_id `12` (C): Annotated start 50 != Inferred start 59
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BootAway` and target `11` (2 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `9` (LB1)
- ❌ Missing segment for action `Action_SecureCatch` on target `14` (RB1)

### Track Identity Issues

- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_ThrowPass' for track '9' has invalid range: start=180, end=117. Clamping end to start.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [42–58], lower_priority='Action_RunBlock' annotated_start=50, effective_Action_RunBlock_start=59.
- ⚠️ Segment 'Action_SecureCatch' for track '14' has invalid range: start=203, end=149. Clamping end to start.
- ⚠️ Action 'Action_RunBlock' range [50-83] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [85-88] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [93-99] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-77] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-111] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-315] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-194] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-134] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [50-82] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [86-90] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [100-108] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [50-125] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-84] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-105] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-63] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-93] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-115] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-70] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [42-55] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [57-58] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [65-80] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [81-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-179] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [59-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-48] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [51-54] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [56-89] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-44] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-57] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-69] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-149] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-85] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-329] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-189] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-170] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-212] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-259] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-282] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-294] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-329] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-296] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-302] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-268] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-242] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-243] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-252] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-241] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-309] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-247] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-251] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-247] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-329] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-268] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-329] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-321] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-305] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-309] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-320] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-329] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-329] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-321] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>