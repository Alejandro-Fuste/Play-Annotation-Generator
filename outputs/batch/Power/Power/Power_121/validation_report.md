# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_121`
- **Input XML**: `outputs/batch/Power/Power/Power_121/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 244: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [9-169] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-187] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-307] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-313] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-317] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-329] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-165] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-161] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-194] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-205] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-225] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-247] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [119-126] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-301] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-154] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-329] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-235] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-242] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-152] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-158] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-161] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-260] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-313] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-309] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-115] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-329] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-141] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-208] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-149] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-160] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-215] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-130] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-149] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-179] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-188] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-323] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-197] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-203] for track '28' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.