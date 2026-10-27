# Play-Annotation-Generator Annotation Review — Counter_316

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_316`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `3` | `2` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_PullLeadBlock` | RB | offense | `4` | `3` |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `22` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 3 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 45 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 112 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `3` | `2` | 110 | START | 110 | 112 |
| ✅ EXACT | `Action_DownBlock` | RT | `1` | `0` | 113 | START | 113 | 192 |
| ✅ EXACT | `Action_DownBlock` | LT | `13` | `12` | 113 | START | 113 | 192 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `3` | `2` | 113 | START | 113 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `9` | `8` | 113 | START | 113 | 161 |
| ✅ EXACT | `Action_PullLeadBlock` | RB | `4` | `3` | 113 | START | 113 | 148 |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | `22` | `17` | 123 | END | 127 | 127 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `6` | 134 | START | 134 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `3` | 153 | START | 176 | 234 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 192 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_Handoff` | 134 | 152 | 19 | inferred_complete_timeline |
| `Action_None` | 153 | 299 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 113 | 148 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 176 | 234 | 59 | inferred_complete_timeline |
| `Action_BallCarry` | 241 | 242 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 3–130
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 109 | 107 | inferred_complete_timeline |
| `Action_None` | 110 | 130 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 192 | 80 | inferred_complete_timeline |
| `Action_None` | 193 | 294 | 102 | inferred_complete_timeline |
| `Action_None` | 297 | 299 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PullBlock` | 113 | 161 | 49 | inferred_complete_timeline |
| `Action_PullBlock` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 181 | 192 | 12 | inferred_complete_timeline |
| `Action_None` | 193 | 267 | 75 | inferred_complete_timeline |
| `Action_None` | 272 | 279 | 8 | inferred_complete_timeline |
| `Action_None` | 291 | 296 | 6 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 45–160
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 74 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 101 | 11 | inferred_complete_timeline |
| `Action_None` | 142 | 146 | 5 | inferred_complete_timeline |
| `Action_None` | 149 | 160 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 299 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 192 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 220 | 111 | inferred_complete_timeline |
| `Action_None` | 228 | 237 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 299 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 245 | 136 | inferred_complete_timeline |
| `Action_None` | 249 | 254 | 6 | inferred_complete_timeline |
| `Action_None` | 267 | 299 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 224 | 115 | inferred_complete_timeline |
| `Action_None` | 227 | 237 | 11 | inferred_complete_timeline |
| `Action_None` | 242 | 254 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 41–299
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 41 | 109 | 69 | inferred_complete_timeline |
| `Action_None` | 110 | 216 | 107 | inferred_complete_timeline |
| `Action_None` | 218 | 248 | 31 | inferred_complete_timeline |
| `Action_None` | 254 | 299 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–189 | 161 | 5 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–145 | 146 | 2 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 122–169 | 42 | 3 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 127–145 | 17 | 3 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 129–299 | 169 | 2 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 133–138 | 6 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 138–299 | 160 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 145–299 | 142 | 3 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 154–299 | 146 | 1 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 179–187 | 9 | 1 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 181–211 | 31 | 1 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 190–196 | 4 | 2 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 191–299 | 92 | 4 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 202–299 | 98 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 204–299 | 96 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 209–232 | 16 | 2 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 221–299 | 76 | 3 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 224–299 | 76 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 254–278 | 24 | 2 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 276–299 | 24 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 284–299 | 16 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 285–299 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '17' has invalid range: start=127, end=123. Clamping end to start.
- ⚠️ Action 'Action_DownBlock' range [113-192] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-116] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [119-124] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [152-189] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [113-148] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [176-234] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [241-242] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-145] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-220] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [113-161] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [166-169] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [172-173] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-267] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-279] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-296] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-224] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-237] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-254] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-245] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-254] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-294] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-130] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-216] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-248] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-47] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-74] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-160] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-169] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 128, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [128-141] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-226] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-138] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-190] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-190] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-187] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-211] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-211] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-238] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-259] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-232] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-229] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-289] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-299] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-278] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-299] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>