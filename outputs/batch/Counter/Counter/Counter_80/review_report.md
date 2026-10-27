# Play-Annotation-Generator Annotation Review — Counter_80

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_80`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 157
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `15` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `15` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `6` | `5` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 5 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `15` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 100 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `15` | `12` | 62 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `10` | `9` | 62 | START | 62 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `15` | `12` | 62 | START | 65 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `7` | `6` | 62 | START | 62 | 99 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `6` | `5` | 62 | START | 62 | 132 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `12` | `11` | 71 | END | 62 | 69 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 82 | START | 82 | 100 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `8` | `7` | 101 | START | 104 | 148 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 132 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 5–146
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 61 | 57 | inferred_complete_timeline |
| `Action_SnapReceive` | 62 | 69 | 8 | inferred_complete_timeline |
| `Action_None` | 74 | 81 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 82 | 100 | 19 | inferred_complete_timeline |
| `Action_None` | 101 | 146 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_BallCarry` | 104 | 148 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–300
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 62 | 132 | 71 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 300 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 74 | 13 | inferred_complete_timeline |
| `Action_None` | 78 | 98 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PullBlock` | 62 | 99 | 38 | inferred_complete_timeline |
| `Action_PullBlock` | 101 | 132 | 32 | inferred_complete_timeline |
| `Action_None` | 133 | 205 | 73 | inferred_complete_timeline |
| `Action_None` | 239 | 264 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 65–290
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_DownBlock` | 65 | 77 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 86 | 89 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 95 | 121 | 27 | inferred_complete_timeline |
| `Action_DownBlock` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 128 | 132 | 5 | inferred_complete_timeline |
| `Action_None` | 133 | 290 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_DownBlock` | 62 | 89 | 28 | inferred_complete_timeline |
| `Action_DownBlock` | 99 | 125 | 27 | inferred_complete_timeline |
| `Action_DownBlock` | 128 | 132 | 5 | inferred_complete_timeline |
| `Action_None` | 133 | 140 | 8 | inferred_complete_timeline |
| `Action_None` | 166 | 172 | 7 | inferred_complete_timeline |
| `Action_None` | 174 | 179 | 6 | inferred_complete_timeline |
| `Action_None` | 187 | 190 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 101 | 40 | inferred_complete_timeline |
| `Action_None` | 106 | 119 | 14 | inferred_complete_timeline |
| `Action_None` | 127 | 213 | 87 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 156 | 95 | inferred_complete_timeline |
| `Action_None` | 232 | 237 | 6 | inferred_complete_timeline |
| `Action_None` | 247 | 269 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 82 | 21 | inferred_complete_timeline |
| `Action_None` | 113 | 124 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 91 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 85 | 24 | inferred_complete_timeline |
| `Action_None` | 90 | 197 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 135 | 74 | inferred_complete_timeline |
| `Action_None` | 154 | 171 | 18 | inferred_complete_timeline |
| `Action_None` | 177 | 179 | 3 | inferred_complete_timeline |
| `Action_None` | 185 | 210 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `16` | Position_Unknown | Team_Unknown | 71–192 | 116 | 2 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 81–100 | 15 | 3 | Undefined position; Undefined team |
| `15` | `21` | Position_Unknown | Team_Unknown | 100–250 | 115 | 3 | Undefined position; Undefined team |
| `16` | `22` | Position_Unknown | Team_Unknown | 103–107 | 5 | 1 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 103–122 | 20 | 1 | Undefined position; Undefined team |
| `18` | `26` | Position_Unknown | Team_Unknown | 112–179 | 68 | 1 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 116–263 | 148 | 1 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 117–199 | 61 | 2 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 120–306 | 154 | 3 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 120–185 | 61 | 2 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 139–140 | 2 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 146–329 | 142 | 8 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 157–207 | 46 | 3 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 161–216 | 49 | 2 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 162–206 | 42 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 163–196 | 34 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 177–277 | 60 | 3 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 191–329 | 133 | 3 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 191–203 | 13 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 194–321 | 120 | 3 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 196–201 | 6 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 196–329 | 110 | 3 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 198–227 | 29 | 2 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 204–329 | 126 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 233–258 | 26 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 235–286 | 52 | 1 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 243–253 | 11 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 248–266 | 19 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 277–329 | 53 | 1 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 298–329 | 31 | 2 | Undefined position; Undefined team |
| `43` | `59` | Position_Unknown | Team_Unknown | 304–329 | 26 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `15` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `7` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `8` (RB): Annotated start 101 != Inferred start 104

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 93 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Overlapping action conflict at frame 62 for track '12': 'Action_BallSnap' vs 'Action_DownBlock'. Overriding with 'Action_DownBlock'.
- ⚠️ Action 'Action_None' range [62-101] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-119] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-213] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-82] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-124] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-91] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-74] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-98] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-156] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-300] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [62-99] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-205] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-264] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [104-148] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-85] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-197] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [62-89] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [99-125] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-172] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-179] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-135] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-171] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [62-69] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [65-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [86-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [95-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [123-124] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-290] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-80] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-192] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-210] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-122] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-263] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-163] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-199] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-186] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-306] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-174] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-185] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-187] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-236] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-247] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-329] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-169] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-207] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-164] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-216] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-181] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-206] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-196] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-218] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-277] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-196] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-287] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-203] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-251] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-279] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-321] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-263] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-295] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-213] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-227] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-258] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-286] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-253] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-266] for track '40' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-301] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-329] for track '43' has 2 frames without a visible bounding box.
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

</details>