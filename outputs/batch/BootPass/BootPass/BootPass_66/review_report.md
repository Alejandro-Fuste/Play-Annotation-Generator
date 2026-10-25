# Play-Annotation-Generator Annotation Review — BootPass_66

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_66`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | OLB1 | defense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_FakeHandoff` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `26` | `22` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `29` | `24` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 0 | START | 0 | 59 |
| ✅ EXACT | `Action_BallSnap` | OLB1 | `10` | `10` | 60 | START | 60 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `0` | `0` | 67 | START | 67 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `12` | `12` | 67 | START | 76 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `3` | `3` | 67 | START | 67 | 84 |
| ✅ EXACT | `Action_RunBlock` | RG | `4` | `4` | 67 | START | 67 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `14` | `14` | 74 | END | 60 | 63 |
| ⚠️ START CHANGED | `Action_FakeHandoff` | QB | `14` | `14` | 82 | START | 97 | 107 |
| ✅ EXACT | `Action_BootAway` | QB | `14` | `14` | 108 | START | 108 | 160 |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `26` | `22` | 145 | START | 145 | 167 |
| ✅ EXACT | `Action_ThrowPass` | QB | `14` | `14` | 167 | START | 167 | 178 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `29` | `24` | 197 | START | 197 | 210 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 59 | 38 | inferred_complete_timeline |
| `Action_SnapReceive` | 60 | 63 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_FakeHandoff` | 97 | 107 | 11 | inferred_complete_timeline |
| `Action_BootAway` | 108 | 160 | 53 | inferred_complete_timeline |
| `Action_None` | 161 | 166 | 6 | inferred_complete_timeline |
| `Action_ThrowPass` | 167 | 178 | 12 | inferred_complete_timeline |
| `Action_None` | 179 | 213 | 35 | inferred_complete_timeline |
| `Action_None` | 218 | 230 | 13 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 101 | 42 | inferred_complete_timeline |
| `Action_None` | 116 | 165 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 87 | 28 | inferred_complete_timeline |
| `Action_None` | 110 | 269 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 269 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_RunBlock` | 76 | 84 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 136 | 143 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_RunBlock` | 67 | 84 | 18 | inferred_complete_timeline |
| `Action_RunBlock` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 101 | 140 | 40 | inferred_complete_timeline |
| `Action_RunBlock` | 143 | 269 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_RunBlock` | 67 | 79 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_RunBlock` | 67 | 125 | 59 | inferred_complete_timeline |
| `Action_RunBlock` | 147 | 148 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 59 | 48 | inferred_complete_timeline |
| `Action_None` | 60 | 91 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 118 | 59 | inferred_complete_timeline |
| `Action_None` | 136 | 197 | 62 | inferred_complete_timeline |
| `Action_None` | 199 | 269 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_BallSnap` | 60 | 74 | 15 | inferred_complete_timeline |
| `Action_None` | 75 | 93 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 72 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>OLB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 163 | 104 | inferred_complete_timeline |
| `Action_None` | 168 | 231 | 64 | inferred_complete_timeline |
| `Action_None` | 237 | 269 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 236 | 177 | inferred_complete_timeline |
| `Action_None` | 255 | 269 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 100 | 41 | inferred_complete_timeline |
| `Action_None` | 112 | 152 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 8–13 | 6 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 18–163 | 18 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 71–269 | 198 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 75–76 | 2 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 80–269 | 190 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 83–152 | 70 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 86–160 | 66 | 4 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 96–269 | 173 | 4 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 101–155 | 55 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 132–269 | 128 | 5 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 143–157 | 15 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 158–268 | 109 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 178–269 | 92 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 226–269 | 44 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 238–269 | 32 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 241–263 | 18 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `14` (2 segments found)
- ⚠️ `Action_FakeHandoff` for actor_track_id `14` (QB): Annotated start 82 != Inferred start 97

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 112: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_RunBlock' range [67-125] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [147-148] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-163] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-231] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [67-84] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [87-88] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [101-140] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [67-79] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-101] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-165] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-87] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-269] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-236] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-100] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-152] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-72] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-118] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-197] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [76-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [136-143] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-91] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [60-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-213] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-230] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-13] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-20] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-163] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-157] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-104] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-155] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-154] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-265] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-157] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-260] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-268] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-259] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '30' has 1 frames without a visible bounding box.
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

</details>