# Play-Annotation-Generator Annotation Review — RPO_103

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `RPO_103`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 153
- **Validation Warnings:** 182
- **Validation Errors:** 1
- **Overall Status:** FAILED
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunHitchGoRoute` | actor_track_id `1` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 14 | START | 14 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 14 | START | 14 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 14 | START | 14 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 14 | START | 14 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 14 | START | 14 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 14 | START | 14 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 14 | START | 14 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 14 | START | 14 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 14 | START | 14 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 14 | START | 14 | 77 |
| ✅ EXACT | `Action_ReadDefender` | QB | `12` | `12` | 25 | START | 25 | 58 |
| ✅ EXACT | `Action_PullBall` | QB | `12` | `12` | 59 | START | 59 | 67 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 87 | START | 87 | 103 |

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
- **Visible Frames:** 14–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 24 | 11 | inferred_complete_timeline |
| `Action_ReadDefender` | 25 | 58 | 34 | inferred_complete_timeline |
| `Action_PullBall` | 59 | 67 | 9 | inferred_complete_timeline |
| `Action_None` | 68 | 86 | 19 | inferred_complete_timeline |
| `Action_ThrowPass` | 87 | 103 | 17 | inferred_complete_timeline |
| `Action_None` | 104 | 269 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 14–33
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 33 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 14–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 269 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 14–257
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 109 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 195 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 246 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 257 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 14–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 269 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 14–111
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 77 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 111 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 14–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 53 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 269 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 14–264
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 85 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 102 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 122 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 144 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 165 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 191 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 202 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 222 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 228 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 248 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 256 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 264 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 14–263
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 32 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 91 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 107 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 154 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 250 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 263 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 14–269
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 54 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 70 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 76 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 100 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 128 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 162 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 251 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 265 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 269 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 14–95
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 95 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 14–119
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 47 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 92 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 119 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 14–138
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 100 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 112 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 119 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 134 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 138 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 14–53
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 53 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 14–95
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 95 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 14–268
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 138 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 148 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 224 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 258 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 268 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 14–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 269 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 14–269
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 108 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 117 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 269 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 14–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 212 | 199 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 269 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 14–202
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 108 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 202 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 14–71
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 41 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 71 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 14–242 | 187 | 9 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 52–269 | 196 | 8 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 104–105 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 121–122 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 141–143 | 3 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 145–269 | 97 | 9 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 146–184 | 39 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 153–269 | 78 | 8 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 157–258 | 57 | 5 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 159–269 | 78 | 7 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 168–254 | 83 | 4 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 170–269 | 89 | 10 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 183–191 | 9 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 189–210 | 21 | 2 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 206–261 | 39 | 3 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 209–269 | 53 | 3 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 226–268 | 40 | 2 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 234–269 | 36 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 252–255 | 4 | 1 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 254–259 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `SAF2` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['C', 'LG', 'LT', 'RG'].

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 138 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 188: Duplicate assignment for track ID '20' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [14-109] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-195] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-246] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-257] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-53] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-95] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-95] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-77] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-111] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-212] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-138] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-148] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-224] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-234] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-258] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-268] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-102] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-153] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-177] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-191] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-209] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-216] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-242] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-269] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-53] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-47] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-92] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-119] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-100] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-112] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-119] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-32] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-91] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-154] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-250] for track '17' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-263] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-33] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-54] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-70] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-100] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-128] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-138] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-151] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-251] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-265] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-41] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-71] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-85] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-102] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-144] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-165] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-191] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-202] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-222] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-228] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-243] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-248] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-256] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-264] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-192] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-207] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-216] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-245] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-253] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-263] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-105] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-122] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-143] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-148] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-204] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-223] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-230] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-237] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-260] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-265] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-184] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-156] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-163] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-219] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-232] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-237] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-169] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-173] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-213] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-252] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-258] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-171] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-192] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-234] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-252] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-265] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-176] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-221] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-248] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-254] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-177] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-203] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-208] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-240] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-243] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-248] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-259] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-263] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-267] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-191] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-194] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-207] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-248] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-261] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-210] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-220] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-269] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-252] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-268] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-255] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-259] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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