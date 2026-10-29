# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_108`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_108/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-196] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-208] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-214] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-218] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-226] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-167] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-175] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-181] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-214] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-239] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-193] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-201] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-181] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-212] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-219] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [179-184] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-195] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-200] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [191-193] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [195-196] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [198-199] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-239] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-229] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.