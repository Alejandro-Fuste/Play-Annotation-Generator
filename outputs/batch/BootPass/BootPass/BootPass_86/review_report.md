# Play-Annotation-Generator Annotation Review — BootPass_86

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_86`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 48
- **Ball Tracks:** 1
- **Action Segments:** 149
- **Validation Warnings:** 183
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 128
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_BootAway` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | TE1 | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `16` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `9` | `Group` | 0 | START | 0 | 67 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 46 | START | 46 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `1` | `1` | 56 | START | 56 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `11` | `11` | 56 | START | 63 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `15` | `15` | 56 | START | 56 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `17` | `17` | 56 | START | 56 | 59 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 62 | END | 46 | 62 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `12` | `12` | 65 | START | 65 | 81 |
| ❌ MISSING SEGMENT | `Action_BootAway` | QB | `12` | `12` | 89 | START | N/A | N/A |
| ✅ EXACT | `Action_ThrowPass` | TE1 | `9` | `9` | 108 | START | 108 | 118 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 62 | 17 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_FakeHandoff` | 65 | 81 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 49 | 4 | inferred_complete_timeline |
| `Action_None` | 52 | 87 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 23 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 45 | 21 | inferred_complete_timeline |
| `Action_None` | 46 | 79 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 87 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 107 | 17 | inferred_complete_timeline |
| `Action_ThrowPass` | 108 | 118 | 11 | inferred_complete_timeline |
| `Action_None` | 119 | 125 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 84 | 39 | inferred_complete_timeline |
| `Action_None` | 86 | 149 | 64 | inferred_complete_timeline |
| `Action_None` | 158 | 166 | 9 | inferred_complete_timeline |
| `Action_None` | 168 | 178 | 11 | inferred_complete_timeline |
| `Action_None` | 183 | 196 | 14 | inferred_complete_timeline |
| `Action_None` | 198 | 286 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_RunBlock` | 56 | 63 | 8 | inferred_complete_timeline |
| `Action_RunBlock` | 72 | 78 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 117 | 119 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_BallSnap` | 46 | 62 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 63 | 73 | 11 | inferred_complete_timeline |
| `Action_RunBlock` | 101 | 123 | 23 | inferred_complete_timeline |
| `Action_RunBlock` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 132 | 145 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_RunBlock` | 56 | 59 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 62 | 90 | 29 | inferred_complete_timeline |
| `Action_RunBlock` | 92 | 110 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_RunBlock` | 56 | 74 | 19 | inferred_complete_timeline |
| `Action_RunBlock` | 76 | 115 | 40 | inferred_complete_timeline |
| `Action_RunBlock` | 119 | 299 | 181 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 195 | 150 | inferred_complete_timeline |
| `Action_None` | 198 | 210 | 13 | inferred_complete_timeline |
| `Action_None` | 212 | 219 | 8 | inferred_complete_timeline |
| `Action_None` | 221 | 232 | 12 | inferred_complete_timeline |
| `Action_None` | 237 | 299 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 79 | 34 | inferred_complete_timeline |
| `Action_None` | 81 | 123 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 85 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 60 | 15 | inferred_complete_timeline |
| `Action_None` | 75 | 86 | 12 | inferred_complete_timeline |
| `Action_None` | 103 | 299 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 99 | 54 | inferred_complete_timeline |
| `Action_None` | 111 | 132 | 22 | inferred_complete_timeline |
| `Action_None` | 149 | 153 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 145 | 100 | inferred_complete_timeline |
| `Action_None` | 148 | 299 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 170 | 125 | inferred_complete_timeline |
| `Action_None` | 175 | 186 | 12 | inferred_complete_timeline |
| `Action_None` | 188 | 299 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 59 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–299 | 298 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 3–195 | 171 | 9 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 78–299 | 165 | 9 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 80–299 | 219 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 88–299 | 212 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 90–93 | 4 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 95–299 | 205 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 128–299 | 171 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 128–299 | 168 | 5 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 132–145 | 14 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 132–299 | 160 | 4 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 143–145 | 3 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 143–259 | 96 | 6 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 145–299 | 138 | 5 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 148–299 | 152 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 149–299 | 148 | 2 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 155–158 | 4 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 161–179 | 8 | 2 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 179–299 | 103 | 5 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 181–299 | 119 | 1 | Undefined position; Undefined team |
| `39` | `43` | Position_Unknown | Team_Unknown | 186–188 | 3 | 1 | Undefined position; Undefined team |
| `40` | `44` | Position_Unknown | Team_Unknown | 192–193 | 2 | 1 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 197–199 | 3 | 1 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 201–203 | 3 | 1 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 202–216 | 15 | 1 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 210–299 | 79 | 3 | Undefined position; Undefined team |
| `45` | `54` | Position_Unknown | Team_Unknown | 246–299 | 49 | 3 | Undefined position; Undefined team |
| `46` | `55` | Position_Unknown | Team_Unknown | 253–266 | 14 | 1 | Undefined position; Undefined team |
| `47` | `56` | Position_Unknown | Team_Unknown | 289–290 | 2 | 1 | Undefined position; Undefined team |
| `48` | `57` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | 0 | 46 | 47 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (6 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `17` (3 segments found)
- ❌ Missing segment for action `Action_BootAway` on target `12` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 117 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 152: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [46–62], lower_priority='Action_RunBlock' annotated_start=56, effective_Action_RunBlock_start=63.
- ⚠️ Segment 'Action_BootAway' for track '12' has invalid range: start=89, end=81. Clamping end to start.
- ⚠️ Action 'Action_None' range [46-59] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [56-74] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [76-115] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [119-299] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-99] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-132] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-195] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-219] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-232] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-82] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-145] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-170] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-186] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-79] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-123] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-84] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-166] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-178] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-196] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-286] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-49] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-87] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [63-73] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [101-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [128-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [132-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [65-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-299] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-85] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [56-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [72-78] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [81-82] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [90-93] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [95-96] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [117-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-23] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-79] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [56-59] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [62-90] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [92-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-4] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-51] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-58] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-153] for track '19' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-184] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-92] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-233] for track '20' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-250] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-275] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-287] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-138] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-157] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-166] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-225] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-296] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-145] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-142] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-256] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-299] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-216] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-234] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-259] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-238] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-299] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-262] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-164] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-212] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-223] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-260] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-278] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-299] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-216] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-299] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-266] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-299] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-266] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.

</details>