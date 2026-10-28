# Play-Annotation-Generator Annotation Review — Draw_60

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_60`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 125
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 52 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 50 | START | 50 | 62 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `12` | `11` | 53 | START | 63 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `2` | `1` | 53 | START | 53 | 163 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `3` | `2` | 53 | START | 53 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `5` | `4` | 53 | START | 53 | 116 |
| ✅ EXACT | `Action_PassBlock` | RT | `8` | `7` | 53 | START | 53 | 163 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 62 | END | 50 | 62 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `11` | `10` | 69 | START | 69 | 93 |
| ✅ EXACT | `Action_BallCarry` | QB | `11` | `10` | 94 | START | 94 | 146 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 163 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_SnapReceive` | 50 | 62 | 13 | inferred_complete_timeline |
| `Action_None` | 63 | 68 | 6 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 69 | 93 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 94 | 146 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 112 | 63 | inferred_complete_timeline |
| `Action_None` | 117 | 121 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 116 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 123 | 163 | 41 | inferred_complete_timeline |
| `Action_None` | 164 | 174 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 163 | 111 | inferred_complete_timeline |
| `Action_None` | 164 | 186 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_BallSnap` | 50 | 62 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 71 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 99 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 163 | 58 | inferred_complete_timeline |
| `Action_None` | 164 | 173 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 163 | 111 | inferred_complete_timeline |
| `Action_None` | 164 | 180 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 105 | 56 | inferred_complete_timeline |
| `Action_None` | 108 | 167 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 129 | 80 | inferred_complete_timeline |
| `Action_None` | 132 | 136 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 188 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–306
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 297 | 248 | inferred_complete_timeline |
| `Action_None` | 300 | 306 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 167 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 256 | 207 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `16` | Position_Unknown | Team_Unknown | 84–160 | 40 | 4 | Undefined position; Undefined team |
| `14` | `20` | Position_Unknown | Team_Unknown | 118–212 | 39 | 4 | Undefined position; Undefined team |
| `15` | `22` | Position_Unknown | Team_Unknown | 132–133 | 2 | 1 | Undefined position; Undefined team |
| `16` | `23` | Position_Unknown | Team_Unknown | 133–134 | 2 | 1 | Undefined position; Undefined team |
| `17` | `26` | Position_Unknown | Team_Unknown | 144–384 | 229 | 4 | Undefined position; Undefined team |
| `18` | `27` | Position_Unknown | Team_Unknown | 146–176 | 31 | 1 | Undefined position; Undefined team |
| `19` | `28` | Position_Unknown | Team_Unknown | 151–260 | 108 | 2 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 152–239 | 88 | 1 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 174–389 | 212 | 3 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 178–389 | 192 | 9 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 222–254 | 30 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 232–389 | 143 | 2 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 235–341 | 104 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 241–265 | 25 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 246–256 | 11 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 276–384 | 47 | 7 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 291–389 | 85 | 3 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 299–300 | 2 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 300–389 | 90 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 304–306 | 3 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 317–389 | 67 | 2 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 323–389 | 67 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 340–389 | 50 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 343–389 | 47 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 351–354 | 4 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 378–389 | 11 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `12` (C): Annotated start 53 != Inferred start 63
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [50–62], lower_priority='Action_PassBlock' annotated_start=53, effective_Action_PassBlock_start=63.
- ⚠️ Action 'Action_None' range [50-129] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-186] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-99] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-103] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-173] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-256] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-116] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-112] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-297] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-306] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-105] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-167] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-167] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [94-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-71] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-88] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-160] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-174] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-212] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-201] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-367] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-375] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-220] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-260] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-323] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-332] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-389] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-222] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-251] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-259] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-362] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-379] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-242] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-254] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-357] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-333] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-341] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-265] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-256] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-288] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-304] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-348] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-355] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-298] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-314] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-306] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-389] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-354] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>