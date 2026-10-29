# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_174`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_174/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-233] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-212] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-193] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-206] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-162] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [127-139] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [146-148] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [150-151] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-168] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-239] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [127-148] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [152-157] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-177] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-187] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-213] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-237] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-22] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-138] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-183] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-192] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-201] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-196] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-206] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-207] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-239] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-239] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.