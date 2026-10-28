# Play-Annotation-Generator Annotation Review — Draw_22

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_22`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 132
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `12` | `11` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | RB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `11` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 30 |
| ✅ EXACT | `Action_BallSnap` | QB | `13` | `12` | 28 | START | 28 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `1` | `0` | 31 | START | 31 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `2` | `1` | 31 | START | 31 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `6` | `5` | 31 | START | 31 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `9` | `8` | 31 | START | 31 | 60 |
| ✅ EXACT | `Action_SnapReceive` | RB | `12` | `11` | 34 | END | 28 | 34 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | RB | `12` | `11` | 38 | START | 38 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `12` | `11` | 69 | START | 69 | 198 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 113 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_BallSnap` | 28 | 34 | 7 | inferred_complete_timeline |
| `Action_None` | 35 | 132 | 98 | inferred_complete_timeline |
| `Action_None` | 138 | 167 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_SnapReceive` | 28 | 34 | 7 | inferred_complete_timeline |
| `Action_None` | 35 | 37 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 38 | 68 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 69 | 198 | 130 | inferred_complete_timeline |
| `Action_BallCarry` | 203 | 237 | 35 | inferred_complete_timeline |
| `Action_BallCarry` | 248 | 251 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 253 | 264 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 266 | 299 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 58 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 103 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_None` | 116 | 143 | 28 | inferred_complete_timeline |
| `Action_None` | 145 | 234 | 90 | inferred_complete_timeline |
| `Action_None` | 245 | 267 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 87 | 57 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 100 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 113 | 4 | inferred_complete_timeline |
| `Action_None` | 114 | 136 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 110 | 80 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 119 | 231 | 113 | inferred_complete_timeline |
| `Action_None` | 249 | 251 | 3 | inferred_complete_timeline |
| `Action_None` | 254 | 299 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 60 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 79 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 124 | 97 | inferred_complete_timeline |
| `Action_None` | 126 | 219 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 52 | 25 | inferred_complete_timeline |
| `Action_None` | 58 | 63 | 6 | inferred_complete_timeline |
| `Action_None` | 73 | 83 | 11 | inferred_complete_timeline |
| `Action_None` | 85 | 199 | 115 | inferred_complete_timeline |
| `Action_None` | 202 | 235 | 34 | inferred_complete_timeline |
| `Action_None` | 238 | 248 | 11 | inferred_complete_timeline |
| `Action_None` | 250 | 254 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 129 | 102 | inferred_complete_timeline |
| `Action_None` | 132 | 240 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 35 | 8 | inferred_complete_timeline |
| `Action_None` | 94 | 153 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 243 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 79 | 52 | inferred_complete_timeline |
| `Action_None` | 84 | 228 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 83 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 23–30 | 8 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 46–151 | 106 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 49–117 | 59 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 75–219 | 145 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 85–193 | 109 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 104–124 | 20 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 105–299 | 190 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 114–222 | 59 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 125–299 | 169 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 128–129 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 134–216 | 83 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 136–299 | 128 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 140–170 | 31 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 163–221 | 57 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 171–299 | 128 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 181–299 | 114 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 182–299 | 118 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 193–299 | 107 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 194–203 | 8 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 199–245 | 47 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 205–279 | 75 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 218–219 | 2 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 255–264 | 10 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 258–299 | 42 | 1 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 262–270 | 9 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 292–299 | 8 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 292–299 | 8 | 1 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 294–299 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 75 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PassBlock' range [31-110] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-231] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [111-113] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-143] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-234] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-267] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-243] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-79] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-228] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-124] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-219] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-87] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [94-100] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [104-105] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-136] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-83] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-240] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-60] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-79] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-35] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-153] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-58] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [69-198] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-237] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [248-251] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [253-264] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-167] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-52] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-63] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-83] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-199] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-235] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-248] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-30] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-117] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-219] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-193] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-278] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-165] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-197] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-237] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-216] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-157] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-222] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-170] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-209] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-221] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-187] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-299] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-299] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-245] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-279] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-264] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-270] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>