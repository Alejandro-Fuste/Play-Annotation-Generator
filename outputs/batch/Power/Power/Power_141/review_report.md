# Play-Annotation-Generator Annotation Review — Power_141

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_141`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 125
- **Validation Warnings:** 151
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 1
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `25` | `19` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `17` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 7 | START | 3 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 7 | START | 3 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 7 | START | 3 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 7 | START | 8 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 7 | START | 8 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `23` | `Group` | 7 | START | 26 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `25` | `Group` | 7 | START | 47 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 7 | START | 3 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 7 | START | 3 | 221 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `13` | `13` | 112 | START | 128 | 129 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `25` | `19` | 112 | START | N/A | N/A |
| ✅ EXACT | `Action_PullBlock` | RG | `17` | `14` | 112 | START | 112 | 119 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 3–178
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 178 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 3–251
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 221 | 219 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 238 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 251 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 3–156
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 156 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 3–329
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 111 | 109 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 133 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 187 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 214 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 222 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 236 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 253 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 302 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 321 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 329 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `23`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 26–329
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 135 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 145 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 186 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 329 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 3–143
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 111 | 109 | inferred_complete_timeline |
| `Action_DownBlock` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 131 | 137 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 142 | 143 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `25`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 47–329
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 47 | 111 | 65 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_None` | 196 | 221 | 26 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 301 | 304 | 4 | inferred_complete_timeline |
| `Action_None` | 306 | 329 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 8–119
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 14 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 20 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 111 | 90 | inferred_complete_timeline |
| `Action_PullBlock` | 112 | 119 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 8–329
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 13 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 111 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 129 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 137 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 145 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 329 | 141 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `27`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `27`
- **team_side:** `defense`
- **Visible Frames:** 81–109
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 81 | 109 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 8–110
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 15 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 110 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `26`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `26`
- **team_side:** `defense`
- **Visible Frames:** 57–179
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 57 | 110 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 179 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 8–137
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 14 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 23 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 111 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 137 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 3–185
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 154 | 152 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 185 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 3–221
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 189 | 187 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 221 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–135
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 129 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 135 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 3–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 329 | 327 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 3–218
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 147 | 145 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 186 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 218 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 3–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 157 | 155 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 172 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 261 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 329 | 66 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 3–329 | 264 | 6 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 3–329 | 327 | 1 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 3–329 | 319 | 3 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 132–329 | 150 | 7 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 184–255 | 68 | 4 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 187–329 | 143 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 191–298 | 83 | 4 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 193–245 | 42 | 3 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 196–243 | 31 | 4 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 197–235 | 36 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 197–329 | 117 | 4 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 200–326 | 127 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 213–329 | 117 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 282–283 | 2 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 283–329 | 27 | 5 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 284–294 | 11 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 326–329 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (3 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `25` (C)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 115 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 284: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [3-222] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-251] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-275] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-278] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-302] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-157] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-172] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-185] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-261] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-147] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-151] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-186] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-218] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-189] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-221] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-221] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-238] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-251] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-185] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-178] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-258] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-111] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-187] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-214] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-222] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-236] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-240] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-253] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-302] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-321] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [128-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [131-137] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [142-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-14] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-20] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-111] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [112-119] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-13] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-111] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-129] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-145] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-329] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-15] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-110] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-14] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-23] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-137] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-145] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-186] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-329] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-111] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-221] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-304] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-179] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-109] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-187] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-227] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-258] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-267] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-206] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-241] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-251] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-255] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-259] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-271] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-292] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-298] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-221] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-241] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-245] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-202] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-215] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-222] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-243] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-230] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-222] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-259] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-285] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-329] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-326] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-329] for track '31' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-283] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-284] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-292] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-304] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-321] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-294] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>