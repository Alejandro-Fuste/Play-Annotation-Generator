# Play-Annotation-Generator Annotation Review — WRSlowScreens_41

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `WRSlowScreens_41`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_WRSlowScreens`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 83
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `26` | `24` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_TurnToQuarterback` | WR1 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReleaseToScreen` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_RunAfterCatch` | WR1 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 4 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `26` | `24` | 2 | START | 106 | 106 |
| ✅ EXACT | `Action_PassBlock` | LG | `17` | `17` | 5 | START | 5 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 5 | START | 5 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `21` | 5 | START | 5 | 38 |
| ✅ EXACT | `Action_PassBlock` | RT | `8` | `8` | 5 | START | 5 | 180 |
| ✅ EXACT | `Action_PassBlock` | LT | `9` | `9` | 5 | START | 5 | 180 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 17 | END | 2 | 17 |
| ✅ EXACT | `Action_TurnToQuarterback` | WR1 | `1` | `1` | 35 | START | 35 | 90 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `20` | `20` | 57 | START | 57 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReleaseToScreen` | LG | `17` | `17` | 59 | START | 59 | 103 |
| ✅ EXACT | `Action_RunAfterCatch` | WR1 | `1` | `1` | 91 | START | 91 | 154 |

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
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 17 | 16 | inferred_complete_timeline |
| `Action_None` | 18 | 56 | 39 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 57 | 74 | 18 | inferred_complete_timeline |
| `Action_None` | 75 | 84 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 103 | 102 | inferred_complete_timeline |
| `Action_None` | 110 | 180 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_TurnToQuarterback` | 35 | 90 | 56 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 91 | 154 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 180 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 180 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 180 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 180 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 58 | 54 | inferred_complete_timeline |
| `Action_ReleaseToScreen` | 59 | 103 | 45 | inferred_complete_timeline |
| `Action_ReleaseToScreen` | 106 | 180 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 38 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 110 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 128 | 124 | inferred_complete_timeline |
| `Action_PassBlock` | 130 | 180 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 180 | 176 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 135 | 134 | inferred_complete_timeline |
| `Action_None` | 137 | 180 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 56 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 60 | 3 | inferred_complete_timeline |
| `Action_None` | 64 | 180 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 53 | 52 | inferred_complete_timeline |
| `Action_None` | 58 | 60 | 3 | inferred_complete_timeline |
| `Action_None` | 66 | 73 | 8 | inferred_complete_timeline |
| `Action_None` | 90 | 97 | 8 | inferred_complete_timeline |
| `Action_None` | 99 | 105 | 7 | inferred_complete_timeline |
| `Action_None` | 109 | 180 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 55 | 54 | inferred_complete_timeline |
| `Action_None` | 58 | 180 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 143 | 142 | inferred_complete_timeline |
| `Action_None` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 170 | 11 | inferred_complete_timeline |
| `Action_None` | 173 | 180 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 180 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 106 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 66 | 65 | inferred_complete_timeline |
| `Action_None` | 68 | 79 | 12 | inferred_complete_timeline |
| `Action_None` | 82 | 109 | 28 | inferred_complete_timeline |
| `Action_None` | 116 | 124 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 145 | 144 | inferred_complete_timeline |
| `Action_None` | 150 | 175 | 26 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 124 | 123 | inferred_complete_timeline |
| `Action_None` | 128 | 158 | 31 | inferred_complete_timeline |
| `Action_None` | 173 | 180 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 157 | 156 | inferred_complete_timeline |
| `Action_None` | 159 | 180 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 44–180 | 123 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 105–168 | 42 | 5 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 106–180 | 61 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 111–180 | 70 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 115–116 | 2 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 153–172 | 20 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 157–170 | 12 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 160–161 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `26` (Position_Unknown): Annotated start 2 != Inferred start 106
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ReleaseToScreen` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 32: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '24' has invalid range: start=106, end=17. Clamping end to start.
- ⚠️ Action 'Action_None' range [2-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [91-154] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-145] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-175] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-170] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-56] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-180] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-135] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-180] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-66] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-79] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-109] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-124] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-106] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-157] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-124] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-158] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-53] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-97] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-180] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-55] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReleaseToScreen' range [59-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReleaseToScreen' range [106-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-180] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-128] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [130-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-84] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-38] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-43] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-110] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-56] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-168] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-119] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-180] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-172] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-170] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '29' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

</details>