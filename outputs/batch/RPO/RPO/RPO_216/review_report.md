# Play-Annotation-Generator Annotation Review — RPO_216

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_216`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 102
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `26` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `10` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 82 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `0` | `0` | 84 | START | 84 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `11` | 84 | START | 84 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `14` | `14` | 84 | START | 84 | 131 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `6` | `6` | 84 | START | 84 | 140 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `9` | `9` | 84 | START | 84 | 140 |
| ✅ EXACT | `Action_ReadDefender` | QB | `5` | `5` | 90 | START | 90 | 108 |
| ✅ EXACT | `Action_PullBall` | QB | `5` | `5` | 109 | START | 109 | 116 |
| ✅ EXACT | `Action_ThrowPass` | QB | `5` | `5` | 134 | START | 134 | 140 |

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
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 89 | 7 | inferred_complete_timeline |
| `Action_ReadDefender` | 90 | 108 | 19 | inferred_complete_timeline |
| `Action_PullBall` | 109 | 116 | 8 | inferred_complete_timeline |
| `Action_None` | 117 | 133 | 17 | inferred_complete_timeline |
| `Action_ThrowPass` | 134 | 140 | 7 | inferred_complete_timeline |
| `Action_None` | 141 | 299 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 115 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 101 | 19 | inferred_complete_timeline |
| `Action_None` | 105 | 299 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 124 | 42 | inferred_complete_timeline |
| `Action_None` | 192 | 232 | 41 | inferred_complete_timeline |
| `Action_None` | 234 | 238 | 5 | inferred_complete_timeline |
| `Action_None` | 240 | 257 | 18 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 265 | 3 | inferred_complete_timeline |
| `Action_None` | 267 | 294 | 28 | inferred_complete_timeline |
| `Action_None` | 296 | 298 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 83 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 131 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 140 | 7 | inferred_complete_timeline |
| `Action_None` | 141 | 299 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 83 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 140 | 57 | inferred_complete_timeline |
| `Action_None` | 141 | 170 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 83 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 120 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 140 | 8 | inferred_complete_timeline |
| `Action_None` | 141 | 178 | 38 | inferred_complete_timeline |
| `Action_None` | 186 | 299 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 83 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 140 | 57 | inferred_complete_timeline |
| `Action_None` | 141 | 154 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 83 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 140 | 57 | inferred_complete_timeline |
| `Action_None` | 141 | 149 | 9 | inferred_complete_timeline |

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
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 92 | 10 | inferred_complete_timeline |
| `Action_None` | 99 | 299 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 167 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_None` | 125 | 164 | 40 | inferred_complete_timeline |
| `Action_None` | 172 | 210 | 39 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_None` | 98 | 169 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 255 | 173 | inferred_complete_timeline |
| `Action_None` | 261 | 271 | 11 | inferred_complete_timeline |
| `Action_None` | 274 | 285 | 12 | inferred_complete_timeline |
| `Action_None` | 287 | 299 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 172 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 159 | 77 | inferred_complete_timeline |
| `Action_None` | 162 | 190 | 29 | inferred_complete_timeline |
| `Action_None` | 192 | 277 | 86 | inferred_complete_timeline |
| `Action_None` | 281 | 282 | 2 | inferred_complete_timeline |
| `Action_None` | 295 | 299 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 299 | 217 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 100–101 | 2 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 102–298 | 197 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 111–164 | 53 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 111–155 | 45 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 140–299 | 160 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 153–157 | 5 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 155–299 | 145 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 157–164 | 5 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 164–172 | 8 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 167–169 | 3 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 179–227 | 49 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 180–225 | 39 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 181–299 | 119 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 196–299 | 104 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 218–221 | 4 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 234–267 | 30 | 2 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 263–266 | 4 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 266–299 | 29 | 2 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 276–299 | 24 | 1 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 290–296 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 61 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [141-149] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-124] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-232] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-257] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-294] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-159] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-190] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-277] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-92] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-299] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '6' starts at frame 141, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [141-154] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-115] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-255] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-271] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-285] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-299] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-170] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-101] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-299] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-178] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-299] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-164] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-210] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-298] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-153] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-164] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-155] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-157] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-299] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-227] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-299] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-267] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-280] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-299] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-296] for track '36' has 1 frames without a visible bounding box.
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

</details>