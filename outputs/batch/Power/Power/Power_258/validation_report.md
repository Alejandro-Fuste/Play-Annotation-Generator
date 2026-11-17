# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_258`
- **Input XML**: `outputs/batch/Power/Power/Power_258/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 515: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - Row 516: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 516: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [13-321] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-271] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-306] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-159] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-205] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-49] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-70] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-160] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-251] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [163-170] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-137] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-339] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-142] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-159] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-172] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-118] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-145] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-238] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-27] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-34] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-52] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-76] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [107-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [117-123] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [131-162] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-108] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-142] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-57] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-74] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-291] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-18] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-26] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-39] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-53] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-72] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-111] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-19] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [107-127] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-359] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-197] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-359] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-208] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-214] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-292] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-228] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-350] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-318] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-264] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-359] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-330] for track '31' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.