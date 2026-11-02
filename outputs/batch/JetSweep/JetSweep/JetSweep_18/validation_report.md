# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `JetSweep_18`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_18/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 25 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_BallSnap' at frame 124 targets track ID '[?]', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 37: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_ZoneBlock' range [130-155] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-163] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [164-174] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-207] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-223] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [130-165] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-169] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-188] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-145] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-178] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-219] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-197] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-157] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-22] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-98] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_Toss' range [144-149] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-159] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [136-138] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [140-171] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-237] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-257] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-5] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-154] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-167] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-170] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-6] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-23] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-131] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-138] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-214] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [150-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-163] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-148] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-169] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-177] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-197] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-212] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-164] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-171] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-243] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-258] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-196] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-200] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-212] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-203] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-234] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-251] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-266] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-229] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-269] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-250] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-255] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-246] for track '30' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.