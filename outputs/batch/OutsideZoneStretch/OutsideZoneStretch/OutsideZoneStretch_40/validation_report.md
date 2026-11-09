# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_40`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_40/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 61 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 82: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [0-186] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-216] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-193] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-196] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-204] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-359] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-218] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-305] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [111-136] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [139-166] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-351] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-234] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-265] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-278] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-325] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-138] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-259] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-172] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-265] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-268] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-276] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-119] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-132] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-256] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-169] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-226] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-154] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-155] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-227] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-167] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-258] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-171] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-240] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-192] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-207] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-227] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-246] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-244] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-250] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-287] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-293] for track '31' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.