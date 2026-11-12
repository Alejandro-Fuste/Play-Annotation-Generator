# Play-Annotation-Generator Annotation Review — SplitZone_218

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_218`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 131
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LB2 | defense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `2` | `2` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | LB1 | defense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_Handoff` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_BallCarry` | LG | offense | `2` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `0` | `Group` | 14 | START | 15 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 14 | START | 15 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 14 | START | 15 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 14 | START | 15 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 14 | START | 15 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 14 | START | 15 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 14 | START | 15 | 93 |
| ✅ EXACT | `Action_BallSnap` | LB2 | `9` | `9` | 91 | START | 91 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `0` | `0` | 94 | START | 94 | 116 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `2` | `2` | 94 | START | 94 | 121 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `4` | `4` | 94 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `8` | 94 | START | 94 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | LB1 | `6` | `6` | 103 | START | 103 | 123 |
| ✅ EXACT | `Action_SnapReceive` | LT | `4` | `4` | 104 | END | 91 | 104 |
| ✅ EXACT | `Action_Handoff` | LT | `4` | `4` | 112 | START | 112 | 121 |
| ✅ EXACT | `Action_BallCarry` | LG | `2` | `2` | 122 | START | 122 | 131 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 204 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 15–219
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 90 | 76 | inferred_complete_timeline |
| `Action_None` | 91 | 179 | 89 | inferred_complete_timeline |
| `Action_None` | 185 | 219 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 15–198
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 90 | 76 | inferred_complete_timeline |
| `Action_None` | 91 | 107 | 17 | inferred_complete_timeline |
| `Action_None` | 111 | 184 | 74 | inferred_complete_timeline |
| `Action_None` | 190 | 198 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 15–356
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 90 | 76 | inferred_complete_timeline |
| `Action_None` | 91 | 141 | 51 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 236 | 307 | 72 | inferred_complete_timeline |
| `Action_None` | 315 | 328 | 14 | inferred_complete_timeline |
| `Action_None` | 355 | 356 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 15–173
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 90 | 76 | inferred_complete_timeline |
| `Action_SnapReceive` | 91 | 104 | 14 | inferred_complete_timeline |
| `Action_None` | 105 | 111 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 112 | 121 | 10 | inferred_complete_timeline |
| `Action_None` | 122 | 173 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 15–131
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 93 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 121 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 122 | 131 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 15–220
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 93 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 116 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 212 | 5 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 220 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 15–359
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 93 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 110 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 166 | 50 | inferred_complete_timeline |
| `Action_None` | 256 | 288 | 33 | inferred_complete_timeline |
| `Action_None` | 290 | 359 | 70 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 15–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 90 | 76 | inferred_complete_timeline |
| `Action_None` | 91 | 135 | 45 | inferred_complete_timeline |
| `Action_None` | 137 | 359 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 15–338
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 90 | 76 | inferred_complete_timeline |
| `Action_None` | 91 | 109 | 19 | inferred_complete_timeline |
| `Action_None` | 138 | 284 | 147 | inferred_complete_timeline |
| `Action_None` | 294 | 338 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 15–187
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 20 | 6 | inferred_complete_timeline |
| `Action_None` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_None` | 113 | 126 | 14 | inferred_complete_timeline |
| `Action_None` | 129 | 177 | 49 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 15–204
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 90 | 76 | inferred_complete_timeline |
| `Action_None` | 91 | 111 | 21 | inferred_complete_timeline |
| `Action_None` | 138 | 204 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 15–184
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 102 | 88 | inferred_complete_timeline |
| `Action_SplitBlock` | 103 | 123 | 21 | inferred_complete_timeline |
| `Action_SplitBlock` | 125 | 138 | 14 | inferred_complete_timeline |
| `Action_SplitBlock` | 141 | 184 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 15–144
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 90 | 76 | inferred_complete_timeline |
| `Action_BallSnap` | 91 | 104 | 14 | inferred_complete_timeline |
| `Action_None` | 105 | 144 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 15–167
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 90 | 76 | inferred_complete_timeline |
| `Action_None` | 91 | 167 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 15–215
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 90 | 76 | inferred_complete_timeline |
| `Action_None` | 91 | 215 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 116–209 | 43 | 4 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 151–359 | 189 | 3 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 169–359 | 189 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 169–359 | 88 | 5 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 174–208 | 31 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 174–216 | 37 | 3 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 179–359 | 173 | 3 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 186–359 | 174 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 191–224 | 34 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 200–359 | 152 | 4 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 222–359 | 138 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 224–237 | 14 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 248–359 | 107 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 258–359 | 87 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 259–359 | 91 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 273–359 | 87 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 276–359 | 83 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 285–359 | 75 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 300–359 | 60 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 306–359 | 54 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 316–321 | 6 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 335–344 | 7 | 2 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 349–351 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `0` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `4` (LT)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '0' (RG) duration 111 frames exceeds threshold 90 frames [start=94, end=204].
- ⚠️ Segment 'Action_ZoneBlock' for track '4' has invalid range: start=94, end=90. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (RT) duration 111 frames exceeds threshold 90 frames [start=94, end=204].
- ⚠️ Action 'Action_ZoneBlock' range [94-116] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [160-161] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-220] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-141] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-307] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-328] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [122-131] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-107] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-184] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-198] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-173] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-109] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-284] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-338] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [103-123] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [125-138] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [141-184] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-93] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-166] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-288] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-359] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-144] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-215] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-179] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-219] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-204] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-20] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-177] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-190] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-209] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-359] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-187] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-211] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-246] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-353] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-199] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-216] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-192] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-359] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-359] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-224] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-241] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-328] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-237] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-282] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-275] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-359] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-345] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-303] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-359] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-321] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-337] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-344] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-351] for track '38' has 1 frames without a visible bounding box.
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

</details>