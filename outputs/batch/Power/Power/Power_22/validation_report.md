# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_22`
- **Input XML**: `outputs/batch/Power/Power/Power_22/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 49 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [17-161] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-196] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-201] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-169] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-176] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-155] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-163] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [91-110] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [118-157] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-188] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-194] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-156] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-103] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-133] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-172] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-113] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-182] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-190] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-192] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-182] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-197] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-201] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-196] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-210] for track '23' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.