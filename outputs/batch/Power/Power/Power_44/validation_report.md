# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_44`
- **Input XML**: `outputs/batch/Power/Power/Power_44/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_None' range [203-229] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-68] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-287] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-191] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-359] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-196] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-241] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-187] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-195] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-359] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-231] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-254] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [162-172] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-296] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-165] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-173] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-245] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-352] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-185] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-217] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-201] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-209] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-293] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-203] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-223] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-228] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-244] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-260] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-287] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-335] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-353] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-273] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-277] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-354] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-285] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-359] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-304] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-311] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-314] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-317] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-348] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-302] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-316] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-322] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-343] for track '34' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.