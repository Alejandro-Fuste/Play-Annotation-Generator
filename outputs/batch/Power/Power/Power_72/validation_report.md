# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_72`
- **Input XML**: `outputs/batch/Power/Power/Power_72/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 37 |
| Ball Tracks | 1 |
| CSV events parsed | 10 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 146: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 146: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [20-300] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-311] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-321] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-157] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-128] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-151] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-112] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-149] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-257] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-265] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-269] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-154] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-295] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-303] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-329] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [95-127] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-171] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-122] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-174] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-171] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-258] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-283] for track '11' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-307] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-124] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-154] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-128] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-251] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-139] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-94] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [95-96] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-160] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-80] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-84] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-112] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-162] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-124] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-128] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-138] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-152] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-164] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-139] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-143] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-151] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-226] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-272] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-281] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-285] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-289] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-323] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-326] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-202] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-171] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-176] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-192] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-275] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-265] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-308] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-329] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-271] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-304] for track '32' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-320] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-300] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-300] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-304] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-309] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-324] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-302] for track '36' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.