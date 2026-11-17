# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_13`
- **Input XML**: `outputs/batch/Power/Power/Power_13/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [14-149] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-239] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-161] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-173] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-195] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-194] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-176] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-118] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-181] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-189] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-205] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-209] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-214] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-218] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-152] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-229] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-214] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-224] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-198] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-196] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-216] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-162] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-220] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-93] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-152] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-169] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-160] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-212] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-216] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-223] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-233] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-236] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-169] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-189] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-171] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-184] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-201] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-212] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-224] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-178] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-214] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-225] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-187] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-196] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '33' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.