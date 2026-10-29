# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_157`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_157/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 51 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ComboBlock' for track '19' has invalid range: start=112, end=98. Clamping end to start.
> - Action 'Action_PreSnap' range [0-158] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-209] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-194] for track '4' has 8 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-209] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-189] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-209] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-202] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-105] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-203] for track '13' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-186] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '16' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [123-181] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-198] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-209] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-185] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-200] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-209] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-119] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-124] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-137] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-195] for track '24' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-133] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-189] for track '26' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-199] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-158] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-209] for track '29' has 1 frames without a visible bounding box.
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