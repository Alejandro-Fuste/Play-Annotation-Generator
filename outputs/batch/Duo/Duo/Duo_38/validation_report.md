# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_38`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_38/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-69] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [167-206] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [209-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-184] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-190] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-217] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [167-193] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [202-203] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [205-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-48] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [167-226] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-227] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-236] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-159] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [167-239] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-191] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-79] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-158] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-185] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-189] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-99] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-162] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-167] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-212] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-234] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-200] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-211] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-219] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-238] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-225] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-234] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-229] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-239] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-239] for track '27' has 5 frames without a visible bounding box.
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
> - Action event 'Action_None' has invalid start frame 240. Video range is [0, 239].

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.