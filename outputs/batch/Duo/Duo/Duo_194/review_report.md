# Play-Annotation-Generator Annotation Review — Duo_194

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_194`
- **Frame Range:** 0 to 249 (250 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 249
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 135
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | LG | offense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_ComboBlock` | RT | offense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | RG | offense | `21` | `21` |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | C | offense | `18` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 202 |
| ✅ EXACT | `Action_ComboBlock` | LG | `14` | `14` | 108 | START | 108 | 120 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | C | `18` | `18` | 108 | START | N/A | N/A |
| ✅ EXACT | `Action_ComboBlock` | RT | `20` | `20` | 108 | START | 108 | 119 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | RG | `21` | `21` | 108 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | C | `18` | `18` | 120 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 145 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 125 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 135 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 162 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 216 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 233 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 208 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 212 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 223 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 249 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 157 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 213 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 223 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 239 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 245 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 207 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_ComboBlock` | 108 | 120 | 13 | inferred_complete_timeline |
| `Action_None` | 179 | 201 | 23 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 217 | 4 | inferred_complete_timeline |
| `Action_None` | 220 | 249 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 185 | 190 | 6 | inferred_complete_timeline |
| `Action_None` | 194 | 198 | 5 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 236 | 247 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_ComboBlock` | 108 | 119 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 192 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 201 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 205 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 249 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 123 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 145 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 187 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 144 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 126 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 172 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 208 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 219 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 181 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 111–183 | 4 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 163–249 | 75 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 174–237 | 32 | 4 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 179–232 | 44 | 4 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 182–249 | 68 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 183–229 | 47 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 188–249 | 33 | 3 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 188–247 | 45 | 4 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 198–245 | 34 | 3 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 199–203 | 5 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 230–241 | 8 | 3 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 230–245 | 15 | 2 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 231–247 | 17 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 235–247 | 12 | 2 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 235–245 | 9 | 3 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 240–245 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ComboBlock` on target `18` (C)
- ❌ Missing segment for action `Action_ComboBlock` on target `21` (RG)
- ❌ Missing segment for action `Action_BlockSecondLevel` on target `18` (C)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 101 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 249 as fallback play end.
- ⚠️ Segment 'Action_ComboBlock' for track '21' has invalid range: start=108, end=102. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-112] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-123] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-145] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-148] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-151] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-172] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-175] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-187] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-192] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-201] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-205] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-161] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-166] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-208] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-212] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-223] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-249] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-202] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-249] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-172] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-208] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-219] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-181] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-146] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-157] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-213] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-223] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-242] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-245] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [108-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-201] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-249] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-183] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-207] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-190] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-198] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-247] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-162] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-216] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-233] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [108-119] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-183] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-164] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-177] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-183] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-207] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-237] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-219] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-229] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-195] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-249] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-205] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-218] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-223] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-247] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-208] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-218] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-245] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-203] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-232] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-241] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-237] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-245] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-247] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-242] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-247] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-241] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-245] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-242] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-245] for track '37' has 1 frames without a visible bounding box.
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

</details>