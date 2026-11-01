# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `InsideZoneStretch_6`
- **Input XML**: `outputs/batch/InsideZoneStretch/InsideZoneStretch/InsideZoneStretch_6/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 126 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_SnapReceive' at frame 129 targets track ID '?', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action_BallSnap present in CSV, but paired Action_SnapReceive is missing.
> - Action 'Action_None' range [175-203] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-273] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-284] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-321] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-216] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-222] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-176] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-155] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-389] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-165] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-185] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-202] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-236] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-364] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [123-277] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-289] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-303] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [123-167] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-201] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-291] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-202] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-266] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-277] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-254] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-265] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [136-149] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-300] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-61] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-64] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-68] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-106] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-136] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [172-182] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [197-218] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [246-247] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [266-296] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-6] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-21] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-27] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [142-173] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-293] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-126] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-135] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '16' starts at frame 136, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [136-136] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [148-162] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-287] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [172-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-146] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [155-206] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-187] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-213] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-281] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-316] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-234] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-238] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-251] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-278] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-289] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-321] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-340] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-389] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-259] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-231] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-274] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-231] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-295] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [298-319] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-327] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-271] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-263] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-273] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-262] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-269] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-279] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [281-312] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [315-340] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-335] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-350] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-357] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-329] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-388] for track '43' has 1 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.