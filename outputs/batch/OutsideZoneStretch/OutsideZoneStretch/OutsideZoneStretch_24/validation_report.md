# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_24`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_24/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 36 |
| Ball Tracks | 1 |
| CSV events parsed | 14 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 50: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [0-221] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-238] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-249] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-263] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-245] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-178] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-192] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-219] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-223] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-232] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-249] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-254] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-234] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-389] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-228] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-269] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-206] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-217] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-229] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-340] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-347] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-389] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-234] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-251] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-178] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-192] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-220] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-257] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_Handoff' range [151-167] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-208] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-215] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-218] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-242] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-137] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-143] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-188] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-198] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-217] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-229] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-247] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-191] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-238] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-203] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-207] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-219] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-319] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-324] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-352] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-369] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-377] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [382-386] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-353] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-365] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [383-384] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-359] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-359] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-381] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [384-389] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-379] for track '33' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.