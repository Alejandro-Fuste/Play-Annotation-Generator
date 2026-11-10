# Play-Annotation-Generator Annotation Review — RPO_117

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_117`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 126
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunFadeRoute` | actor_track_id `6` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_RunBlock` | RT | offense | `17` | `17` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 5 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 5 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 5 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 5 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 5 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 5 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 5 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 5 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 5 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 5 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 5 | START | 0 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `13` | `13` | 74 | START | 80 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `14` | `14` | 74 | START | 75 | 76 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | LG | `15` | `15` | 74 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `16` | `16` | 74 | START | 77 | 78 |
| ⚠️ START CHANGED | `Action_RunBlock` | RT | `17` | `17` | 74 | START | 115 | 128 |
| ✅ EXACT | `Action_ReadDefender` | QB | `5` | `5` | 77 | START | 77 | 83 |
| ✅ EXACT | `Action_PullBall` | QB | `5` | `5` | 84 | START | 84 | 94 |
| ✅ EXACT | `Action_ThrowPass` | QB | `5` | `5` | 125 | START | 125 | 133 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 76 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 77 | 83 | 7 | inferred_complete_timeline |
| `Action_PullBall` | 84 | 94 | 11 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 124 | 24 | inferred_complete_timeline |
| `Action_ThrowPass` | 125 | 133 | 9 | inferred_complete_timeline |
| `Action_None` | 134 | 143 | 10 | inferred_complete_timeline |
| `Action_None` | 149 | 239 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 97 | 25 | inferred_complete_timeline |
| `Action_None` | 101 | 107 | 7 | inferred_complete_timeline |
| `Action_None` | 117 | 125 | 9 | inferred_complete_timeline |
| `Action_None` | 145 | 161 | 17 | inferred_complete_timeline |
| `Action_None` | 164 | 189 | 26 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_None` | 202 | 239 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 121 | 49 | inferred_complete_timeline |
| `Action_None` | 127 | 142 | 16 | inferred_complete_timeline |
| `Action_None` | 144 | 164 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 107 | 35 | inferred_complete_timeline |
| `Action_None` | 110 | 129 | 20 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 142 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 239 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 90 | 18 | inferred_complete_timeline |
| `Action_None` | 105 | 132 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_RunBlock` | 80 | 85 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 101 | 103 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 116 | 133 | 18 | inferred_complete_timeline |
| `Action_None` | 134 | 137 | 4 | inferred_complete_timeline |
| `Action_None` | 187 | 212 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 114 | 123 | 10 | inferred_complete_timeline |
| `Action_RunBlock` | 125 | 132 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_RunBlock` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 116 | 127 | 12 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 146 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_RunBlock` | 115 | 128 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `22`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 21–61
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 25 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 35 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 43 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 51 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 61 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 164 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 142 | 70 | inferred_complete_timeline |
| `Action_None` | 149 | 162 | 14 | inferred_complete_timeline |
| `Action_None` | 165 | 168 | 4 | inferred_complete_timeline |
| `Action_None` | 172 | 183 | 12 | inferred_complete_timeline |
| `Action_None` | 185 | 239 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 206 | 134 | inferred_complete_timeline |
| `Action_None` | 211 | 239 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 239 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 185 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 239 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 186 | 114 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `24` | Position_Unknown | Team_Unknown | 24–62 | 7 | 3 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 72–141 | 27 | 4 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 116–239 | 110 | 4 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 120–174 | 22 | 4 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 151–153 | 3 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 159–239 | 77 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 168–237 | 65 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 180–205 | 18 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 183–239 | 56 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 185–187 | 3 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 186–238 | 49 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 189–239 | 46 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 192–239 | 48 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 201–239 | 39 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 202–218 | 7 | 2 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 203–232 | 13 | 3 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 204–215 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `14` (3 segments found)
- ❌ Missing segment for action `Action_RunBlock` on target `15` (LG)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `16` (2 segments found)
- ⚠️ `Action_RunBlock` for actor_track_id `17` (RT): Annotated start 74 != Inferred start 115

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 90 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_RunBlock' for track '15' has invalid range: start=74, end=65. Clamping end to start.
- ⚠️ Action 'Action_None' range [73-107] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-129] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-107] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-125] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-161] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-189] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-239] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-164] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-164] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-186] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-206] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-90] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-132] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-162] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-183] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [80-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [101-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-212] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 73, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [73-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [75-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [114-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [125-132] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [77-78] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [116-127] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [115-128] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-25] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-35] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-43] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-51] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-50] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-62] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '21' starts at frame 73, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [73-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-141] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-239] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-128] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-174] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-223] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-237] for track '26' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-205] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-199] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-238] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-239] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-239] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-239] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-220] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '36' has 1 frames without a visible bounding box.
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

</details>