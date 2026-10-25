# Play-Annotation-Generator Annotation Review — BootPass_132

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_132`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 32
- **Ball Tracks:** 1
- **Action Segments:** 80
- **Validation Warnings:** 91
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 4
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `33` | `25` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | LT | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `10` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `13` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 23 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | `8` | `8` | 16 | END | N/A | N/A |
| ✅ EXACT | `Action_FakeHandoff` | QB | `8` | `8` | 24 | START | 24 | 50 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 41 | START | 41 | 41 |
| ✅ EXACT | `Action_BootAway` | QB | `8` | `8` | 51 | START | 51 | 67 |
| ❌ MISSING SEGMENT | `Action_RunFlatRoute` | Position_Unknown | `33` | `25` | 60 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | `15` | `15` | 90 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | LT | `12` | `12` | 111 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_FakeHandoff` | 24 | 50 | 27 | inferred_complete_timeline |
| `Action_BootAway` | 51 | 67 | 17 | inferred_complete_timeline |
| `Action_None` | 68 | 71 | 4 | inferred_complete_timeline |
| `Action_None` | 77 | 92 | 16 | inferred_complete_timeline |
| `Action_None` | 95 | 105 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 74 | 34 | inferred_complete_timeline |
| `Action_None` | 77 | 159 | 83 | inferred_complete_timeline |
| `Action_None` | 162 | 164 | 3 | inferred_complete_timeline |
| `Action_None` | 168 | 174 | 7 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_None` | 185 | 199 | 15 | inferred_complete_timeline |
| `Action_None` | 202 | 204 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 110 | 70 | inferred_complete_timeline |
| `Action_None` | 115 | 334 | 220 | inferred_complete_timeline |
| `Action_None` | 338 | 359 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 102 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 108 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_BallSnap` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_None` | 42 | 112 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 119 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 93 | 53 | inferred_complete_timeline |
| `Action_None` | 98 | 130 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 68 | 28 | inferred_complete_timeline |
| `Action_None` | 70 | 98 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 79 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 125 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 107 | 67 | inferred_complete_timeline |
| `Action_None` | 109 | 226 | 118 | inferred_complete_timeline |
| `Action_None` | 231 | 241 | 11 | inferred_complete_timeline |
| `Action_None` | 244 | 301 | 58 | inferred_complete_timeline |
| `Action_None` | 304 | 359 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 359 | 319 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 359 | 319 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 104 | 64 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 47–48 | 2 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 57–100 | 44 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 79–314 | 202 | 4 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 104–151 | 48 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 137–251 | 114 | 2 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 159–359 | 162 | 2 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 175–346 | 172 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 178–359 | 179 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 185–359 | 170 | 3 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 189–359 | 171 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 203–359 | 157 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 241–359 | 119 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 244–359 | 115 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 266–359 | 81 | 5 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 313–359 | 32 | 2 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 357–358 | 2 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 359–359 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `19` | `25` | 126 | 138 | 4 | 30.8% | 127, 130–137 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SnapReceive` on target `8` (QB)
- ❌ Missing segment for action `Action_RunFlatRoute` on target `25` (Position_Unknown)
- ❌ Missing segment for action `Action_ThrowPass` on target `15` (Position_Unknown)
- ❌ Missing segment for action `Action_SecureCatch` on target `12` (LT)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 113, Column 'Run Block': Could not parse frame number from '-' in entry '-,OL'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '8' has invalid range: start=41, end=16. Clamping end to start.
- ⚠️ Segment 'Action_SecureCatch' for track '12' has invalid range: start=111, end=102. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '14' has invalid range: start=41, end=16. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '15' has invalid range: start=90, end=48. Clamping end to start.
- ⚠️ Action 'Action_None' range [41-104] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-79] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-107] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-226] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-241] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-301] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-93] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-130] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-119] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-71] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-92] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-105] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-98] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-74] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-174] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-199] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-125] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-110] for track '13' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-334] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-48] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-230] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-290] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-246] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-295] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-359] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-346] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-351] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-278] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-359] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-287] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-296] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-351] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-324] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>